from agentique.agents.chunk_agent import ChunkAgent
from agentique.agents.lieutenant_agent import LieutenantAgent
from agentique.agents.SOA_agent import SOA_agent

import os
import openai
import asyncio
from dotenv import load_dotenv 

load_dotenv() 



le_client = openai.AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)
le_model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

texte = """
-	Petit chenapan, fait attention à la dame !
-	J’ai pas fait exprès m’man !
Sarah excusa d’un signe de main l’enfant qui venait de la bousculer. Elle, qui n’avait jusqu’ici connu que le calme de son monastère, était émerveillée par le tourbillon de vie qui pouvait émaner d’une grande ville. Ici, un marchand de babioles ventripotent négociait avec un vieux monsieur renfrogné, là des enfants se pourchassaient dans la rue en criant. Une odeur forte de poisson se mêlait avec discordance au parfum raffiné d’épices exotiques. Et si la prêche d’un orateur était interrompue par le braiement d’un âne, elle n’était reprise que par l’éclat de rire bruyant d’un commerçant ou par les cliquetis d’une charrette sur les pavés irréguliers de la ville.
-	Ces mômes me rendent fous. Au moins, nous arrivons.
Sarah jeta un œil à son grommelant compagnon. Sa haute carrure et sa démarche tranchante inspiraient une assurance certaine, soulignée par la lourde épée qui pendait à ses côtés. Cependant, le colosse n’était manifestement pas à l’aise au milieu de toute cette foule. Son regard alerte et ses membres tendus témoignaient d’une volonté pressante de quitter ce labyrinthe de corps et de cris auquel aucun entraînement militaire ne l’avait préparé.
-	Tu vas donc arrêter de grogner ? le taquina Sarah.
Elle ne connaissait Bill Bolivar que depuis quelques jours, et pourtant, lui vouait déjà une admiration sans borne. Aussi, comment aurait-il pu en être autrement ? Pour une jeune prêtresse de Margaux comme elle, il aurait déjà été difficile de ne pas être fascinée par ce guerrier quadragénaire, dont le corps portait la marque d’une carrière militaire aussi longue que brillante. 
Mais ce qui rendait Bill particulièrement exceptionnel, c’était la décision qu’il avait prise : laisser derrière lui sa vie de soldat pour consacrer entièrement son épée à la déesse.
Et ce n’était ni par lassitude, ni par contrainte. Après tant d’années passées au sein de l’armée impériale, il n’y reconnaissait simplement plus les idéaux qui l’avaient autrefois amené à s’engager. Le commandement inhumain et les exactions qui s’y banalisaient l’avaient poussé à quitter son régiment. Son départ était sa révolte. Sa foi, la continuité de son engagement.
Pour une jeune clergesse ayant décidé de quitter le monastère dans le but de faire l’expérience du monde, marcher aux côtés d’un tel homme relevait de la providence. Elle pouvait s’estimer bien chanceuse d’avoir à ses côtés un mentor d’exception prêt à lui montrer la voie le moment venu.
Mais en attendant, c’est elle qui l’avait convaincu d’aller payer leurs respects au temple local de Margaux pour chercher conseil avant cette importante journée. Aussi, ses sourcils se froncèrent quand elle aperçut un petit groupe de gardes en armes qui semblait bloquer les portes du temple.
D’une démarche vive, elle s’approcha d’un petit soldat moustachu qui semblait être en charge.
-	Bonjour Sergent, pourriez-vous m’indiquer ce qu’il se passe ? Nous désirons nous joindre à la messe de ce matin. Cela est-il encore possible ?
-	Ah non Mademoiselle ! Toutes mes excuses mais le temple est fermé pour la matinée par arrêté de Monseigneur le commandant de la garde.
Sarah le regarda avec dépit.
-	Croyez-moi bien, cela me navre profondément d’interdire l’accès au temple en un jour aussi solennel mais les circonstances sont telles qu’il est impossible de faire autrement. Soyez assurée que nous faisons tout notre possible pour que l’activité puisse reprendre au plus vite. 
-	 Ah oui ! rétorqua Bill. Et peut-on avoir plus d’informations sur ces fameuses circonstances qui nécessiteraient une fermeture complète du temple ?
Le soldat, pas intimidé pour un sou malgré la taille colossale de son interlocuteur, répondit calmement à la question :
-	Je ne suis pas censé divulguer ces informations pour le moment, hésita-t-il, mais du fait de votre affiliation au clergé de Margaux, je vais vous en faire la faveur. 
Le petit homme enroula distraitement son doigt dans sa moustache. 
-	Après tout, vous semblez être d’honorables personnes ; je vous fais confiance pour ne pas colporter des rumeurs qui ne pourraient que nuire à la réputation de votre ordre.
-	Bien sûr, acquiesça Bill
Sarah sourit discrètement. Il était difficile de dire ce qui déliait le plus la langue du sergent entre l’épée de Margaux qui ornait leurs habits et le ton péremptoire de Bill. Ou peut-être était-il tout simplement d’un naturel bavard…
-	Très bien. Alors voilà. Il semblerait que le grand prêtre ait disparu, révéla-t-il à mi-voix. Cela fait suite à une série de disparitions que nous surveillions de loin. Cependant, le fait que cela affecte maintenant un personnage d’une telle importance a poussé le commandement à prendre des mesures d’ampleur pour élucider l’affaire au plus vite.
-	Et alors ? 
-	Et alors voilà où nous en sommes. Ecoutez, si cette affaire vous intéresse, allez voir le capitaine Bongranvil. C’est lui qui s’occupe de tout. Et, il sera probablement ravi de pouvoir vous donner de plus amples détails.
Le sergent semblait de toute évidence ne pas en savoir davantage. Même si la curiosité la tiraillait, Sarah préféra le remercier pour le temps qu’il avait bien voulu leur accorder et quitter les lieux.
-	Tu penses qu’ils vont le retrouver ? demanda-t-elle à Bill. Ça semble un peu inquiétant. J’espère qu’il ne leur est rien arrivé de trop grave.
Toute cette affaire semblait bien mystérieuse. Que pouvait-il bien être arrivé ? Elle essayait d’imaginer les causes possibles de cet événement mais rien ne semblait faire sens. Elle examina l’expression de son compagnon mais celui-ci ne paraissait guère préoccupé.
-	Tu sais, fillette, beaucoup de choses peuvent amener un homme à laisser derrière lui son quotidien… 
Que signifiait cette phrase sibylline ? Devant son air interrogateur, Bill développa sa pensée.
-	Certes, quelque fois, c’est contre son gré qu’on est tiré hors de sa vie bien ordonnée. Mais bien souvent on ne fait qu’embrasser une opportunité qui nous est offerte. Tu vois ce que je veux dire ?
Il haussa les épaules et se remit à marcher à grandes enjambées.
-	 A observer l’homme depuis maintenant quelques années, je me suis rendu compte qu’il est rare d’en voir un qui ne saurait abandonner son office pour telle ou telle raison. Il se satisfait de rien et surtout pas du carcan qu’on cherche à lui imposer. L’homme est changeant et imparfait, c’est ce qui fait sa beauté. 
Il marqua un temps d’arrêt, un sourire cynique au visage.
-	Mais bon, pour répondre à ta question, je mettrais bien une pièce sur le fait qu’il sera retrouvé dans 2 ou 3 jours dans une position fort inconfortable pour une personnalité de son calibre. Bien sûr, l’affaire sera étouffée par les autorités, comme toujours.
Sarah ne fut pas très convaincue par ces paroles. Après avoir passé l’essentiel de sa vie dans un monastère de Margaux, elle s’était forgé cette conviction que rien n’était plus intraitable que l’esprit d’un vieux religieux séculier. A force de prêcher toute leur vie les mérites d’un combat contre les vices et le chaos, ces derniers acquerraient une force de caractère et une résilience à toute épreuve. Pour elle, les plus anciens du culte représentaient vraiment la souche inattaquable qui soutenait l’intégrité de l’ensemble de l’ordre. Elle voyait mal comment une telle âme aurait pu être détournée de sa tâche pour quelque raison que ce soit. 
Cependant, elle n’osa pas en faire la remarque à son ainé. Après tout, après des années à servir au côté des troupes de l’Empire, Bill Bolivar avait certainement ses raisons d’avoir une vision aussi pessimiste de la moralité des grands de ce monde.
Sarah songeait encore aux paroles de son comparse tandis qu’ils débouchaient sur la grande avenue de Vinfort. Une file interminable se dirigeait vers le château qui, au loin, surplombait la ville. Les riches carrosses se mêlaient sans gêne à une foule de badauds qui tentaient de se frayer un chemin à travers la procession. Le soleil se réfléchissait avec grâce sur les riches parures des aristocrates parfois venus de l’autre côté de la grande mer. Une douce brise agitait les bannières de différentes délégations. Sarah reconnut l’ours de Bélême, le cerf de Nyrhion, les armoiries de Freydearn. Et là-bas, au loin, n’était-ce pas Follier en personne qui venait représenter le royaume d’Al-Quazir ? Tout ce beau monde qui se massait aux portes de Vinfort ! Et ce temps magnifique ! La fête du solstice de cette année semblait prometteuse.
Néanmoins, Sarah ne put s’empêcher de noter une certaine agitation parmi certaines délégations. Des sourcils froncés et des mines sombres s’échangeaient messes basses et regards soucieux. Un voile indescriptible semblait planer sur la procession, telle l’atmosphère lourde d’une nuit d’août. 
Bien sûr, elle avait entendu les rumeurs d’une éventuelle offensive impériale, « Le retour de la grande guerre », comme le criaient les agitateurs les plus audacieux. Jusqu’ici, elle n’y avait pas porté trop d’attention. Ce genre de rumeurs était monnaie courante et pas une semaine ne passait sans que le récit de quelques exactions impériales ou de toute autre menace sur les Jeunes Royaumes n’arrivât à ses oreilles. En effet, bien que beaucoup d’eau ait coulé sous les ponts depuis la dernière grande guerre, guerre qui s’était d’ailleurs achevée au pieds des murailles mêmes où la jeune prêtresse se trouvait, les tensions politiques avec l’Empire éteaient encore bien présentes et le sentiment anti-impérialiste était vraisemblablement le seul dénominateur commun à tous les habitants des Jeunes Royaumes.
Cependant, cette fois-ci, peut-être était-ce différent. En tout cas, ce n’était vraisemblablement pas un hasard si la plupart des vieux alliés de Vinfort se rassemblaient aujourd’hui. Et même si la fête du solstice avait toujours attiré intrigants et négociants des deux continents, Sarah ne se faisait pas d’illusion : Vinfort allait aujourd’hui être le siège de tractations politiques parmi les plus importantes de ces dernières années.
Était-ce donc pour cela qu’on lui avait demandé de rejoindre le château de Vinfort aujourd’hui ?  Aura-t-elle un rôle à jouer dans les événements qui s’annonçaient ? Cela semblait peu probable. Après tout, elle n’était qu’une jeune prêtresse bien peu expérimentée : elle voyait mal comment elle pourrait être d’une quelconque aide. De plus, Vinfort ne semblait pas manquer de clercs aguerris qui seraient certainement honorés d’être appelé directement à la cour baronniale. Pourtant, à l’idée de pouvoir enfin se rendre utile, de pouvoir enfin faire quelque chose, quelque chose qui sorte du cadre restreint, familier, sempiternel et tellement répétitif de son monastère, elle ne pouvait s’empêcher d’exulter.
 Pendant bien longtemps, elle avait demandé aux révérends de son monastère de lui permettre de sortir, d’explorer le continent, avant de se consacrer entièrement à son ordre. Après tout, les voies de Margaux sont plurielles. Peut-être n’est-ce pas en tant que moniale qu’elle servirait au mieux son ordre. Comment le saurait-elle sans en connaître davantage sur le monde qui l’entoure ? Et comment pourrait-elle insuffler à d’autres le courage d’affronter leur destin et de mener leurs batailles si elle-même n’avait jamais eu l’occasion de mener sa propre vie.
En tout cas, ces efforts n’avaient pas été vains, et arrivée aux portes de l’enceinte du château, elle eut la fierté de pouvoir s’annoncer aux gardes de la manière la plus officielle qu’il soit :
-	Bonjour, je suis Sarah Hautegarde, nous avons été convoqués aujourd’hui par le baron Boisson de Vinfort. Des consignes doivent nous attendre ici.
-	Bien sûr mademoiselle, veuillez me suivre.
Ils furent conduits assez prestement jusqu’à une antichambre richement décorée. Des tapisseries illustrant les exploits de la noble maison de Vinfort recouvraient l’entièreté des murs. Des larges fenêtres laissaient la lumière du matin baigner la salle d’une douce lumière. Un homme enveloppé dans une cape violette se tenait dans un coin de la salle, le dos tourné, dédaignant les bancs en velours vermillon qui ne semblaient pourtant qu’attendre un occupant.
Lors de leur entrée dans la salle, l’individu se retourna et les salua maladroitement. Sarah ne put s’empêcher de noter son teint bleuté ainsi que les deux petits appendices sur son crâne. Cela l’intrigua, mais ce n’était pas la première fois qu’elle rencontrait des personnages au physique aussi inhabituel.
-	Said, thaumaturge et illusionniste. Puissent mes talents vous être utile.
-	Enchantée, vous aussi vous avez aussi été convoqué par le baron ?
-	Oui, enfin… oui c’est cela, répondit-il d’une voix hésitante.
-	Vous venez de loin ?
-	Hum. Pourquoi cela vous intéresse-t-il ? De loin, de près, je suis ici maintenant.
-	Cela m’intrigue c’est tout. Je n’ai jamais eu l’occasion de rencontrer quelqu’un comme vous. Comment vous êtes-vous retrouvé à Vinfort ?
Après un nouveau soupir de Said, Sarah décida d’abandonner la partie, l’inconnu était définitivement peu loquace et ne semblait pas enclin à discuter davantage. Sarah s’assit donc à côté de Bill qui semblait plongé dans ses pensées. Ou bien s’était-il peut-être assoupi ? Elle avait entendu dire que certains soldats impériaux étaient entraînés à dormir dès qu’ils avaient un temps de repos. Elle sortit de la poche de sa robe son livre de prières. Elle le connaissait presque par cœur maintenant ; mais cela la réconfortait toujours de parcourir ses textes sacrés. 
Elle fut interrompue après un certain temps par l’irruption d’une jeune fille aux longs cheveux hirsutes qui entra dans la salle en courant
-	Wow, c’est géant ici ! Tout ce rouge ! Regarde Lulu, tu as vu le gros dragon dessiné là ! Oh des gens ! Bonjour tout le monde. Je m’appelle Cuera. Et la grincheuse là, c’est Lulu. Je plaisante Lulu. T’es grave sympa en vrai. Eh toi, pourquoi t’es tout bleu ?
 Une elfe assez âgée à l’ossature généreuse pénétra dans la salle. Elle semblait épuisée par sa jeune compagne.
-	Excusez là. Elle est encore jeune et impertinente. Cuera, s’il-te-plaît, laisse le monsieur tranquille, tu vois bien que tu le déranges.
Said lui lança un regard reconnaissant tandis qu’elle s’asseyait lourdement non loin de Sarah.
-	Eh bien ! Que de monde aujourd’hui ! Tout ça parce que l’année est finie et qu’une nouvelle débute. N’est-ce pas un peu exagéré ? Plus personne n’a le moindre souci de la mesure aujourd’hui.
-	C’est important de fêter les grands moments de l’année non ? s’étonna Sarah. Et c’est rassembleur. Ça rappelle un peu aux gens qu’ils ont une place dans une société plus grande qu’eux, qu’ils ne sont pas seuls, qu’ils vivent pour quelque chose. 
-	Peuh ! Orgie et déboires ; et aux frais d’une administration qui se soucie davantage du contrôle de ses sujets que de ce qui leur est vraiment utile. Je vais vous dire moi, car j’en ai une longue expérience personnelle : Prenez n’importe quel enfant, tant que vous le divertissez, il vous mangera dans la main. Mais dès que vous cherchez à l’instruire…. Les hommes ne sont tous que des grands enfants.
-	Lulu ! Laisse un peu les gens s’amuser, l’interrompit Cuera. Profite un peu, il fait beau, on est reçu par un baron, on est dans une pièce sublime… C’est trop bien ! Pourquoi tu es toujours aussi grognon ?
Sarah sembla apercevoir un mouvement dans la chevelure de la jeune fille mais n’y préta pas attention. Cette dernière s’était passionnée pour un chandelier mural et semblait se demander à quel point elle pouvait le dévisser avant que l’ensemble ne tombe au sol. Elle semblait si vivante et si enjouée que Sarah ne put s’empêcher de sourire. Même Bill sortit de sa médiation et se mêla à leur discussion.
 Ainsi, ils apprirent que les nouvelles arrivantes s’étaient rencontrées un peu par hasard sur les routes. Si c’est Cuera qui avait été appelé nominativement par le Baron, il semblait évident que Lulu estimait qu’il était de sa responsabilité personnelle de prendre soin d’elle. L’elfe leur raconta sa vie d’avant, l’école dont elle s’occupait, les enfants qu’elle avait à charge, et finalement sa volonté de sortir, de s’échapper de cet environnement qu’elle ne supportait plus. « Tout cela pour me retrouver à veiller à nouveau sur une gamine. On est toujours rattrapé par ce que l’on fuit », plaisanta-t-elle.	 Cuera prenait ces boutades avec enjouement. Rien ne semblait pouvoir effacer sa vivacité et son entrain naturel. Aussi, fut-elle la première à sauter de sa banquette quand une servante vint les chercher pour les introduire au Baron.
Si l’antichambre où ils avaient patienté était richement décorée, rien ne pouvait les avoir préparés au faste de la salle d’honneur. Dès son arrivée, Sarah fut frappée par l’éclat doré qui rayonnait de toute la pièce et se réfléchissait sur d’immenses miroirs muraux aux cadres finement ciselés. Des personnages antiques, aux regards sévères, semblaient observer la scène du haut de leurs tapisserie. 
Sur un parquet de noyer ancien se tenait une longue table en acajou, recouverte d’une nappe damassée aux couleurs de la maison. Les restes d’un banquet aussi sophistiqué qu’exubérant trônaient dans une riche vaisselle en argent. 
Au loin, présidant la table, un homme à la haute stature semblait plongé dans ses pensées. Sa barbe finement taillée et sa chevelure grisonnante annonçaient un quarantenaire confiant, habitué à se faire écouter et obéir. Il était vêtu d’un surcot de velours sombre ainsi que d’une fine cape en hermine. Et avec le blason qui ornait ses vêtements, il n’y avait aucun doute : Sarah avait devant-elle le baron Boisson de Vinfort.
 Ce dernier mit quelques instants à noter l’entrée de ses nouveaux hôtes. Il se leva alors calmement et les accueillit avec un grand sourire.
-	Mes amis ! Quel plaisir de vous voir ! Enfin une lumière au bout du tunnel ! Mais je vous en prie, installez-vous !
Sarah exécuta une courbette un peu maladroite. Malgré son air avenant, le baron l’intimidait, ou tout au moins était-elle effrayée à l’idée de commettre un impair devant une telle figure. En jetant un œil aux autres invités, elle observa qu’ils étaient tous plutôt à l’aise. Seul Said se tenait en retrait et semblait tout faire pour ne pas attirer l’attention.
Le baron s’assit à la grande table et les invita d’un geste à prendre place à côté de lui.
-	Eh bien ! On m’avait raconté tout le meilleur de vous et je ne suis pas déçu. Je vous remercie d’avoir répondu à mon appel. Comment allez-vous ? Le voyage n’a pas été trop long ? Je sais que certains d’entre vous viennent de loin.
-	Merci à vous de nous recevoir Monseigneur, répondit Bill. Le voyage s’est très bien passé et nous sommes tous impatients de découvrir ce pourquoi vous nous avez fait venir.
-	Je n’en doute pas, s’esclaffa le baron. En même temps, vous venez tous d’horizons divers, vous ne vous connaissez pas, et vous vous retrouvez ici en entrevue avec un puissant seigneur qui est sur le point de vous annoncer qu’il a désespérément besoin de vos talents. Mais ne vous inquiétez pas, tout cela est prévu. Vous êtes pile là où vous devez être. Et les plans qui vous concernent ont été mûrement réfléchis.
-	Des plans ? l’interrompit Lulu. Et en quoi cela consisterait-il ? Comment le souverain d’un des plus puissants des Jeunes Royaumes se retrouve à avoir besoin d’une bande hétéroclite comprenant des gamines à peine en âge de s’occuper d’elles-mêmes ? Et en plus, qui vous dit que j’accepterais, moi, de rentrer dans vos petites cases ? Je vous trouve bien arrogant monsieur le baron.
Si le ton aussi agressif de l’elfe surpris leur interlocuteur, celui-ci n’en laissa rien paraître. Il lui répondit du tac au tac sans se départir de son grand sourire.
-	Ah ! Je suis bien content que vous ayez décidé de nous rejoindre ! Vous posez des questions extrêmement pertinentes. Cette équipe manquait d’une touche de révolte, et s’y j’ose dire, d’impertinence.  Ecoutez, autant que j’apprécie votre présence ici, rien ne vous force à vous engager auprès de moi, ni aucun de vos compagnons d’ailleurs. En revanche, si vous acceptez de travailler pour moi, je saurais évidemment me montrer généreux en retour ; cela va de soi. Mais je suis certain que cette motivation purement matérielle est superflue. Si vous êtes là, c’est que d’une manière ou d’un autre, vous rechercher l’aventure. Prendre les routes, vivre des événements exceptionnels, servir Vinfort, c’est aussi cela que je vous offre. Bien des jeunes écuyers pleins d’audace, donneraient beaucoup pour être à votre place. Mais c’est à vous que je donne cette chance, car c’est de vous dont j’ai besoin. Pourquoi ? J’allais y venir. Mais avant tout je me demande : A quel point êtes-vous au courant de la situation géopolitique actuelle ? Connaissez-vous nos ennemis ? nos amis ? Que se passe-t-il ? Quels sont les enjeux du moment ?
Sarah fut assez surprise par ces questions. N’étant jamais trop sorti de son monastère, sa seule connaissance du monde venait des nouvelles qui arrivaient de manière éparse par quelques visiteurs. Elle avait toujours aimé discuter et débattre des conflits avec l’empire et des inclinations politiques de tel ou tel royaume.
Malheureusement, si elle avait déjà parcouru quelques livres parlant de géographie ou d’histoire, ses connaissances de la politique actuelle étaient assez limitées. Aussi, fut-elle assez soulagée quand Bill prit la parole.
-	Cela fait maintenant 6 mois que j’ai quitté l’armée impériale. Personne ne savait ce qui allait se passer mais il était évident que l’activité s’intensifiait. Les entraînements étaient plus rudes. Les hauts-officiers étaient occupés. Il me semblait évident qu’une campagne se préparait.
-	Vous n’êtes donc pas au courant, le coupa Vinfort. Mes chers amis, la cité d’Olynthienne est tombée il y a de cela 2 semaines. La nouvelle ne devrait pas tarder à se répandre mais le pire est à craindre. On parle en effet d’une immense armée qui se masserait à nos portes. Les relations avec l’Empire sont au plus bas. Les frontières sont quasiment fermées, même le commerce est au point mort.
Un silence de mort s’abattit sur l’assistance. Cela faisait des décennies qu’une paix fragile s’était établit entre l’Empire et ses voisins orientaux. Néanmoins, si Olynthienne était passé sous le giron impérial, cela ne pouvait annoncer qu’une seule chose : les querelles politiques avaient finalement éclos en un conflit ouvert qui s’annonçait aussi long que meurtrier.
-	C’était donc pour cela cette réunion ? hasarda Sarah. L’alliance des jeunes Royaumes va se reformer ? Encore une fois ?
-	C’est plus compliqué que cela, soupira Vinfort. Le rapport de force n’a jamais été aussi défavorable. Et il est de plus en plus difficile de convaincre les autres de nous rejoindre. Vinfort a pour tradition de se dresser contre l’expansion orientale de l’Empire. Par le passé, trois fois ont-ils pénétré nos frontières. Trois fois nous les avons repoussés. Mais aujourd’hui, je ne sais plus sur qui compter. Les autres royaumes sont effrayés bien sûr. Et Follier, dont le soutien est primordial, semble jouer un double jeu. Je ne sais pas si je peux lui faire confiance.
Follier... On racontait qu’elle tenait à elle seule le royaume d’Al-Quazir, plus puissante que le roi lui-même. Officiellement, ce serait une mage, tenant une place de conseillère privilégiée. Mais on l’accusait de l’usage des pires formes de sorcellerie pour satisfaire sa soif de pouvoir.
-	Et qu’est-ce que cela a à faire avec nous, demanda Lulu. Nous ne sommes pas des combattants ou des politiciens. Comment comptez-vous qu’on règle vos problèmes ? 
Sarah balaya rapidement la table du regard. Autour de Vinfort et de son sourire plein d’assurance se tenaient en tout et pour tout un déserteur de l’empire, un prestidigitateur un peu louche, une vieille elfe corpulente, une jeune adolescente et elle, une jeune prêtresse tout aussi inexpérimentée. Il était difficile de croire que c’était sur ce genre d’individus que Vinfort fondait tous ses espoirs.
-	Ah, si seulement il suffisait de quelques âmes déterminées pour résoudre n’importe quelle situation ! soupira Vinfort. Non, bien sûr, je ne me repose pas entièrement sur vous. Votre travail se placera dans un cadre bien plus large. Beaucoup de sacrifices ont déjà été consentis pour la réalisation de cette opération ; et nous étions même sur le point de parvenir à nos fins. Malheureusement, la soudaineté des récents événements a quelque peu bouleversé tout ce qui avait été programmé. Enfin bon, gouverner c’est s’adapter n'est-ce pas ?
Le visage du baron sembla s’obscurcir un court instant. De tout évidence, cette affaire l’inquiétait au plus haut point.
-	M’enfin, ça ne nous dit toujours pas pourquoi vous avez besoin de nous, s’exclama Cuera la bouche à moitié pleine d’un gâteau qu’elle avait piqué sur la table. C’est vrai quoi ! Vous avez pas des super espions, des preux chevaliers ou des mercenaires intrépides pour les situations comme ça ?
Vinfort sourit gentiment. 
-	 Ce n’est pas aussi simple. Vous pouvez être sûrs que nous avons étudié avec attention un large panel de scénarios. Si c’est cette option qui a été retenue, c’est bien parce que c’est celle qui a le plus de chance de fonctionner.
Le baron se gratte la tête avant de reprendre.
-	Comme vous vous en doutez, Olynthienne est extrêmement surveillée. On ne peut pas y faire entrer n’importe qui et l’accès y serait très difficile pour la plupart de mes hommes. De plus, j’ai de bonnes raisons de penser que l’Empire a accès à un réseau très performant au sein même de mon palais. Mais vous, vous êtes intraçables ! Personne ne vous a jamais vu en contact avec un officier ou un fonctionnaire de Vinfort. Et vous avez chacun des motifs personnels qui justifieraient le fait de prendre la route et de vous installer pour une durée indéterminée à Olynthienne.
Quelque chose derrière l’attitude confiante de Vinfort trahissait une certaine inquiétude, comme l’impression de jouer contre un adversaire qui avait toujours un coup d’avance. Il semblait fixer un à un ses interlocuteurs comme s’il se demandait lequel allait lui faire faux bond. Derrière son assurance affichée, Vinfort était désespéré.
-	Parce que c’est ça que vous attendez de nous, l’interrompit Bill. Vous nous jetez dans la gueule du loup, en plein dans une ville qui vient tout juste d’être prise par la force militaire la plus puissante du continent, pullulant encore probablement de tout un tas de soldats et de mercenaires. Vous savez à quoi ça ressemble une ville qui vient de tomber ? Pauvreté, criminalité, commerce souterrain, violence, répression. Et encore, ça c’est dans le cas où elle n’a pas été rasé, brûlé ou pillée. Et vous comptez y envoyer des enfants ? Déjà moi, s’il y a bien deux choses que je n’ai pas envie de vivre, c’est le siège d’une ville et ses conséquences.
-	Eh bien tout va bien alors parce qu’il n’y a pas eu de siège, le coupa Vinfort avec calme.
-	Comment ça pas de siège ? ricana Bill. La ville s’est rendue toute seule peut-être ?
-	Nous ne savons pas exactement. Ecoutez, comme je vous l’ai dit, il est très difficile de savoir ce qui se passe de l’autre côté des montagnes. Ce qui est sûr c’est que le seigneur d’Olynthienne est décédé et a été remplacé par un étranger qui a immédiatement fait allégeance à l’Empire. Tout le reste n’est que rumeurs et suppositions…
Les invités s’échangèrent des regards. Olynthienne avait toujours été une ville assez mystérieuse. Souvent elle était moquée dans les Jeunes Royaumes pour son excentricité. Située quasiment à la frontière avec les terres impériales, elle entretenait avec l’Empire des relations quasi-cordiales. Evidemment, cette accointance était extrêmement profitable à la cité qui s’enrichissait considérablement de son rôle d’interface entre Orient et Occident.
Néanmoins, si la ville d’Olynthienne était clairement le Jeune Royaume le plus proche de l’Empire, Sarah était relativement sûre qu’aucun rapprochement n’avait jamais été envisagé. Olynthienne s’était d’ailleurs battu avec acharnement pour son indépendance au cours des 3 dernières guerres et ce revirement brutal était clairement des plus suspects.
-	Après, comme je vous l’ai déjà dit, je ne vous force pas à vous engager dans cette aventure. Je ne cherche pas à vous en cacher les risques tout comme je n’en minimise pas l’importance. Je vous donnerai tout mon soutien pour le succès de cette entreprise. Evidemment, j’attends de vous en retour une loyauté indéfectible et une implacabilité à la tâche.
Un court silence parcouru l’assemblée. L’attitude solennelle du baron contrastait assez largement avec l’enthousiasme tout relatif de son auditoire. Si le souverain dominait la table de sa haute stature, engageant tout son corps dans un discours passionné, ses invités ne partageaient clairement pas son engouement. Sarah avait du mal à décider lequel de ses interlocuteurs semblait le plus réticent à s’engager sur la voie qui leur avait été toute tracée. 
D’une part, au plus près de leur vénérable hôte, Bill et Lulu, les anciens du groupe, paraissaient recourir à des trésors d’ingénierie pour montrer au baron une hostilité contrôlée, tout juste assez retenue pour ne pas franchir le seuil de l’irrespect, mais indiscutablement, irrémédiablement et définitivement opposée à ses projets.
 De l’autre, Said et Cuera semblaient particulièrement en retrait. Tandis que le premier écoutait attentivement les interventions de chacun, en évitant néanmoins autant que possible les regards, la plus jeune d’entre eux ne prêtait qu’une attention très limitée à la discussion ; elle s’attaquait maintenant à son plat de résistance : une belle cuisse de poulet qu’elle dévorait méthodiquement.
Le baron se leva 
-	Eh bien, c’est décidé donc. Vous partez demain à l’aube. Je vais laisser à mon aide de camp le soin de vous expliquer tous les détails de l’expédition. Je suis sûr que vous saurez vous montrez à la hauteur de la tâche qui vous attend.
-	Attendez, protesta Lulu, je ne …
-	Ah oui, c’est vrai, l’interrompit Vinfort avec un sourire. Je ne vous ai pas dit de quoi il retournait précisément. Vous devrez juste récupérer un objet, un coffre en fait. Je laisse Artès vous donnez tous les détails mais, je vous demande un chose : quoiqu’il arrive, ne l’ouvrez pas.
-	Ce n’est pas…
-	Ne l’ouvrez pas. C’est tout.
Vinfort quitta la salle laissant son assistance interdite. Un silence étrange s’installa seulement interrompu par le craquement sec de la cuisse de poulet que Cuera continuait de mâchonner.  	
-	Nan mais quel toupet, s’indigna Lulu. Pour qui si prend-il au juste ?
Sarah comprenait l’énervement de la vieille elfe. Après tout, sous ses airs avenants, Vinfort ne leur laissait pas vraiment le choix ; et ils se trouvaient maintenant embarqués dans une expédition dont l’ampleur les dépassait complètement.
-	Si je puis me permettre, murmura Said, il me semble que l’offre du seigneur Vinfort devrait être considérée avec attention. Après tout, il me semble qu’ont été avancés des points très pertinents qui justifient pleinement notre engagement potentiel dans cette mission...
Ses propos se perdirent tandis qu’un homme à la démarche militaire faisait son entrée. Complètement chauve, son crâne brillant plongea immédiatement la grande salle dans une atmosphère grave et sérieuse qui effaça presque instantanément l’animosité des convives. 
-	Artès Clairvald, lieutenant d’ordonnance de monseigneur Vinfort, se présenta-t-il. Je suis chargé de vous exposer les termes de la mission.
Il étala sur la table une grande carte couverte d’annotations en patte de mouche et leur fit une présentation détaillée sur la voie qu’ils devraient emprunter pour rejoindre Olynthienne. Sarah fut impressionnée par l’implacabilité de son intervention. Tout s’orchestrait avec une logique et une précision remarquable. Rien n’était laissé au hasard. Les diverses questions de Bill étaient traitées en quelques mots avec détachement et assurance. C’était là un homme qui connaissait son sujet parfaitement.
Une fois qu’il les eut fait traverser les montagnes et pénétrer à l’intérieur de l’enceinte de la ville, il les conduisit à travers les subtilités de leur mission. Il leur décrivit synthétiquement l’organisation de la ville, ce qu’il savait des jeux de pouvoirs plus ou moins officiels et leur transmis le peu de nouvelles depuis la prise de la ville. Il leur donna également quelques informations pour reconnaître le fameux coffre et leur parla d’un point de chute au cœur d’Olynthienne d’où ils pourraient mener leurs opérations. Tout le groupe buvait avidement ses paroles, ne perdant pas une miette des précieuses informations qui leur étaient divulguées.
-	C’est une opération audacieuse, conclut-il, mais nous pensons que vous êtes à même de la mener à succès. Je vous vois demain à l’aube pour les derniers préparatifs. Profitez bien de votre dernière journée à Vinfort. Demain, une grande aventure commence.
Il se leva, replia ses cartes et sortit de la salle.
-	Fiouuu, soupira Cuera, j’ai bien cru qu’il ne s’arrêterait jamais. Et Olynthienne par-ci, et l’Empire par-là ; et bli, et bla. Au final, c’est pas si compliqué : on arrive, on cherche, on trouve, et on rentre. Et on visite un peu quand même ! Elle a l’air trop géniale, cette ville !
L’enthousiasme de la jeune fille prêtait à sourire. Néanmoins, la tâche qui les attendait était loin d’être aussi simple. En marchant, pour quitter le palais, Sarah fit le point sur la situation. 
On les avait lancés sur les traces d’un coffre à peine long d’un pied, perdu dans l’une des plus grandes villes du continent. Artès leur avait décrit une cité aussi effervescente que tentaculaire. Véritable ruche humaine, la métropole abritait plusieurs dizaines de milliers d’âmes auxquelles s’ajoutait un flot incessant de marchands, de vagabonds et d’itinérants en tout genre, qui y transitaient toute l’année pour leurs affaires. 
Et comme si cela ne suffisait pas, après avoir retrouvé l’objet, il leur faudrait encore l’exfiltrer hors d’Olynthienne, au nez et à la barbe des Impériaux qui venaient tout juste de prendre le contrôle des lieux.
 Leurs atouts ? Quelques vagues informations sur un mercenaire de Vinfort, qui aurait mis la main sur le coffre et dont on n’était sans nouvelles depuis 2 semaines.
-	D’ailleurs, qu’est-ce qui nous dit que ce que cherche Vinfort n’est pas déjà sorti de la ville ? demanda Sarah. Ça fait un bout de temps que l’Empire a pris possession des lieux. Si ça se trouve, le coffre est déjà loin.
Said se racla la gorge et prit la parole d’une voix hésitante.
-	Hum, en fait, c’est une hypothèse assez peu probable. D’après ce que Monsieur Clairvald a laissé entendre, il y a fort à parier que le coffre contienne en réalité un artéfact magique d’une certaine importance.
-	Oh, fit Cuera, c’est vrai ?
Ses yeux pétillaient d’excitation.
-	 Un tel objet distord le plan spirituel, continua Said. Il fait du bruit si vous voulez. A Olynthienne, ce signal est masqué par la ville elle-même. Après tout, ses fondations remontent à bien avant la Fracture et la cité tout entière est profondément imprégnée de magie. Mais si le coffre était dehors… Je suis presque certain que Monseigneur de Vinfort le saurait déjà.
Malgré le ton hésitant de son compagnon au teint bleuté, Sarah ne douta pas un seul instant de ce qu’il venait d’avancer. Un frisson la parcourut. Était-elle vraiment à la hauteur pour une telle mission ? Mais après tout, elle avait si longtemps attendu une telle opportunité. Elle n’allait pas laisser passer sa chance.  
-	Ils n’auraient pas pu évacuer le coffre avant l’arrivée de l’Empire, grommela Lulu. Mais non ! C’était bien mieux d’attendre gentiment quelques milliers de soldats ennemis. Ça aurait été trop facile sinon.
La mauvaise humeur de leur aînée pesait sur l’ensemble du groupe tandis qu’ils sortaient silencieusement de l’enceinte du château.
-	Et toi tu ne dis rien ? fit-elle en se tournant vers Bill. En bon soldat, tu vas faire ce qu’on te demande ?  Sans poser de questions ?
Sarah se demandait comment le paladin allait réagir. L’elfe semblait avoir touché un point sensible. Et si Bill était resté à l’écart du groupe, c’était très probablement justement parce qu’il était encore en train de démêler tout ce qui leur avait été dit.
Il resta encore silencieux quelques secondes puis prit une grande inspiration.
-	Si ce que Vinfort annonce est vrai, il serait insensé de ne pas se ranger à ses côtés. Une invasion impériale, ça serait la mort de milliers d’innocents, des vieillards, des enfants, tous sacrifiés à l’autel d’une domination sans partage. 
Il soupira.
-	Mais je ne fais pas confiance à Vinfort. Quels que soient ses véritables desseins, il nous cache quelque chose. Et je ne lui remettrai pas sur un plateau un objet d’une telle puissance. 
Sarah s’approcha de lui en croisant les bras. 
-	Et qu’est-ce que tu proposes à la place ? Laissez le coffre à Olynthienne ? Vinfort est notre suzerain, je te rappelle. Enfin… le mien en tout cas. C’est notre devoir de suivre sa volonté. 
Autant qu’elle respectait son aînée, Sarah était bien décidée à ne pas lâcher l’affaire cette fois-ci. Après tout ce qu’ils avaient entendus, après la confiance que leur avait témoigné le baron, ils ne pouvaient plus se défiler. Ils iraient à Olynthienne et ramèneraient ce fichu coffre. Coûte que coûte.
Bill se retourna et la regarda dans les yeux ;
-	Mais tu ne comprends pas ? Tous les hommes sont les mêmes dès qu’ils acquièrent ne serait-ce qu’un peu de pouvoir… L’illusion du contrôle, une chimère derrière laquelle ils courent tous. Et ne crois pas que Vinfort se soucie de ses sujets. Il en sacrifierait bien la moitié si cela lui permettait de continuer à régner sur l’autre…
Sarah commença à taper nerveusement du pied. Ils venaient tout juste d’accepter la mission de Vinfort et tout commençait déjà à aller à vaux l’eau. Elle comprenait bien le point de vue de son compagnon, surtout au vu de son passé tumultueux. Mais il devait bien comprendre que la situation était différente. Enfin, c’était de Vinfort dont on parlait.
-	Vinfort compte sur nous, répondit-elle d’un air buté. J’irai jusqu’au bout du voyage.  Que vous le vouliez ou non. Je ne suis pas une traitresse.
"""

texte_2="""
-	Petit chenapan, fait attention à la dame !
-	J’ai pas fait exprès m’man !
Sarah excusa d’un signe de main l’enfant qui venait de la bousculer. Elle, qui n’avait jusqu’ici connu que le calme de son monastère, était émerveillée par le tourbillon de vie qui pouvait émaner d’une grande ville. Ici, un marchand de babioles ventripotent négociait avec un vieux monsieur renfrogné, là des enfants se pourchassaient dans la rue en criant. Une odeur forte de poisson se mêlait avec discordance au parfum raffiné d’épices exotiques. Et si la prêche d’un orateur était interrompue par le braiement d’un âne, elle n’était reprise que par l’éclat de rire bruyant d’un commerçant ou par les cliquetis d’une charrette sur les pavés irréguliers de la ville.
-	Ces mômes me rendent fous. Au moins, nous arrivons.
Sarah jeta un œil à son grommelant compagnon. Sa haute carrure et sa démarche tranchante inspiraient une assurance certaine, soulignée par la lourde épée qui pendait à ses côtés. Cependant, le colosse n’était manifestement pas à l’aise au milieu de toute cette foule. Son regard alerte et ses membres tendus témoignaient d’une volonté pressante de quitter ce labyrinthe de corps et de cris auquel aucun entraînement militaire ne l’avait préparé.
-	Tu vas donc arrêter de grogner ? le taquina Sarah.
Elle ne connaissait Bill Bolivar que depuis quelques jours, et pourtant, lui vouait déjà une admiration sans borne. Aussi, comment aurait-il pu en être autrement ? Pour une jeune prêtresse de Margaux comme elle, il aurait déjà été difficile de ne pas être fascinée par ce guerrier quadragénaire, dont le corps portait la marque d’une carrière militaire aussi longue que brillante. 
Mais ce qui rendait Bill particulièrement exceptionnel, c’était la décision qu’il avait prise : laisser derrière lui sa vie de soldat pour consacrer entièrement son épée à la déesse.
Et ce n’était ni par lassitude, ni par contrainte. Après tant d’années passées au sein de l’armée impériale, il n’y reconnaissait simplement plus les idéaux qui l’avaient autrefois amené à s’engager. Le commandement inhumain et les exactions qui s’y banalisaient l’avaient poussé à quitter son régiment. Son départ était sa révolte. Sa foi, la continuité de son engagement.
Pour une jeune clergesse ayant décidé de quitter le monastère dans le but de faire l’expérience du monde, marcher aux côtés d’un tel homme relevait de la providence. Elle pouvait s’estimer bien chanceuse d’avoir à ses côtés un mentor d’exception prêt à lui montrer la voie le moment venu.
Mais en attendant, c’est elle qui l’avait convaincu d’aller payer leurs respects au temple local de Margaux pour chercher conseil avant cette importante journée. Aussi, ses sourcils se froncèrent quand elle aperçut un petit groupe de gardes en armes qui semblait bloquer les portes du temple.
D’une démarche vive, elle s’approcha d’un petit soldat moustachu qui semblait être en charge.
-	Bonjour Sergent, pourriez-vous m’indiquer ce qu’il se passe ? Nous désirons nous joindre à la messe de ce matin. Cela est-il encore possible ?
-	Ah non Mademoiselle ! Toutes mes excuses mais le temple est fermé pour la matinée par arrêté de Monseigneur le commandant de la garde.
Sarah le regarda avec dépit.
-	Croyez-moi bien, cela me navre profondément d’interdire l’accès au temple en un jour aussi solennel mais les circonstances sont telles qu’il est impossible de faire autrement. Soyez assurée que nous faisons tout notre possible pour que l’activité puisse reprendre au plus vite. 
-	 Ah oui ! rétorqua Bill. Et peut-on avoir plus d’informations sur ces fameuses circonstances qui nécessiteraient une fermeture complète du temple ?
Le soldat, pas intimidé pour un sou malgré la taille colossale de son interlocuteur, répondit calmement à la question :
-	Je ne suis pas censé divulguer ces informations pour le moment, hésita-t-il, mais du fait de votre affiliation au clergé de Margaux, je vais vous en faire la faveur. 
Le petit homme enroula distraitement son doigt dans sa moustache. 
-	Après tout, vous semblez être d’honorables personnes ; je vous fais confiance pour ne pas colporter des rumeurs qui ne pourraient que nuire à la réputation de votre ordre.
-	Bien sûr, acquiesça Bill
Sarah sourit discrètement. Il était difficile de dire ce qui déliait le plus la langue du sergent entre l’épée de Margaux qui ornait leurs habits et le ton péremptoire de Bill. Ou peut-être était-il tout simplement d’un naturel bavard…
-	Très bien. Alors voilà. Il semblerait que le grand prêtre ait disparu, révéla-t-il à mi-voix. Cela fait suite à une série de disparitions que nous surveillions de loin. Cependant, le fait que cela affecte maintenant un personnage d’une telle importance a poussé le commandement à prendre des mesures d’ampleur pour élucider l’affaire au plus vite.
-	Et alors ? 
-	Et alors voilà où nous en sommes. Ecoutez, si cette affaire vous intéresse, allez voir le capitaine Bongranvil. C’est lui qui s’occupe de tout. Et, il sera probablement ravi de pouvoir vous donner de plus amples détails.
Le sergent semblait de toute évidence ne pas en savoir davantage. Même si la curiosité la tiraillait, Sarah préféra le remercier pour le temps qu’il avait bien voulu leur accorder et quitter les lieux.
"""


def get_chunks(texte: str, chunk_size: int = 400, overlap: int = 200) -> list[str]:
    mots = texte.split()
    chunks = []
    for i in range(0, len(mots), chunk_size-overlap):
        chunk = mots[i:i+chunk_size]
        chunks.append(" ".join(chunk))
    return chunks

if __name__ == "__main__":
    chunks = get_chunks(texte_2)
    list_of_chunk_agents=[]
    for chunk in chunks:
        list_of_chunk_agents.append(ChunkAgent(chunk, le_client, model=le_model))

    lieutenant_agent = LieutenantAgent(list_of_chunk_agents, 0, len(list_of_chunk_agents)-1, le_client, model=le_model)
    soa_agent = SOA_agent(le_client, model=le_model)
    user_request = "Résume le texte"
    plan_of_action = asyncio.run(soa_agent.process_message(user_request))
    print(plan_of_action)
    print("--------------------------------")
    print("--------------------------------")
    print("--------------------------------")

    response = asyncio.run(lieutenant_agent.process_message(user_request, plan_of_action))
    print(response)






