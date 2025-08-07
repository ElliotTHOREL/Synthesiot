from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompt.lieutenant_agent import PROMPT_SYSTEM
from agentique.banque_de_prompt.lieutenant_agent import PROMPT_USER_SUMMARY
from agentique.agents.auxtrans import AuxTransAgent
from agentique.agents.com_agent import ComAgent
from agentique.agents.SOA_agent import SOA_agent
from agentique.tools import extract_think_do_block
from agentique.historique_message import Message, ConversationHistory
from agentique.agents.resumeur_agent import ResumeurAgent

import openai
import logging
import asyncio



class LieutenantAgent(BaseAgent):
    def __init__(self, list_of_sub_agents: list[BaseAgent], id_first_sub_agent : int, id_last_sub_agent : int, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.list_of_sub_agents = list_of_sub_agents
        self.id_first_sub_agent=id_first_sub_agent
        self.id_last_sub_agent=id_last_sub_agent
        self.resumeur_agent = ResumeurAgent(id_first_sub_agent, id_last_sub_agent, openai_client, model)
        self.summary = None

        self.system_prompt = PROMPT_SYSTEM

        self.auxtrans_agent = AuxTransAgent(list_of_sub_agents, id_first_sub_agent, id_last_sub_agent, openai_client, model)
        self.com_agent = ComAgent(openai_client, model)

    async def async_init(self):
        sub_agents = self.list_of_sub_agents[self.id_first_sub_agent : self.id_last_sub_agent + 1]
        tasks = [agent.async_init() for agent in sub_agents]
        await asyncio.gather(*tasks)

        self.summary = await self.get_summary()
        self.soa_agent = SOA_agent(self.summary, self.client, self.model)
        

    async def get_summary(self):
        sub_summaries = [agent.summary for agent in self.list_of_sub_agents[self.id_first_sub_agent : self.id_last_sub_agent + 1]]
        return await self.resumeur_agent.process_message(sub_summaries)


    async def process_message(self, user_message: str, max_steps: int = 10) -> str:
        plan_of_action = await self.soa_agent.process_message(user_message)
        self.historic = ConversationHistory()

        fini = False
        nb_ite = 0
        while not fini and nb_ite < max_steps:
            nb_ite += 1
            fini =await self._process_one_step(user_message, plan_of_action)
        
        synthese = await self.com_agent.process_message(user_message, self.historic)
        return synthese

    async def _process_one_step(self, user_message: str, plan_of_action : str):
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content":"Voici le plan d'action du planificateur : \n\n {}".format(plan_of_action)})
        
        for message in self.historic.messages:
            if message.auteur == "lieutenant":
                messages.append({"role": "assistant", "content": message.content})
            elif message.auteur == "synthetiseur":
                messages.append({"role": "assistant", "content": "Réponse de l'agent subalterne : \n\n{}".format(message.content)})
        


        string_response = await self.call_openai(messages)
        dict_response = extract_think_do_block(string_response)
        
        
        self.historic.add_message(Message(auteur="lieutenant", content=string_response))

        if dict_response is None:
            logging.warning(f"Format invalide : {string_response}")
            self.historic.add_message(Message(auteur="lieutenant", content="ERRUER : Format invalide. Respecte le format demandé"))
            return False
        if dict_response["do"] == "READY":
            return True
        elif dict_response["do"] == "QUESTION":
            reponse = await self.auxtrans_agent.process_message(dict_response["question"])
            self.historic.add_message(Message(auteur="synthetiseur", content=reponse))
            return False

        


    



