# iziKlasse
Ce projet fournit une application « examen » qui permet aux utilisateurs de répondre à un quiz de programmation en ligne.

Pour obtenir un aperçu de l'interface Yaksh, veuillez vous référer à la documentation utilisateur sur [Yaksh Docs](http://yaksh.readthedocs.io/)

Ceci est un guide de démarrage rapide pour aider les utilisateurs à configurer une instance d'essai. Si vous souhaitez déployer Yaksh dans un environnement de production voici un [Guide de déploiement en production](https://github.com/chaieb-adel/iziKlasse/blob/main/README_production.rst)

[](https://github.com/FOSSEE/online_test#introduction)introduction
------------------------------------------------------------------

Ce projet fournit une application « examen » qui permet aux utilisateurs de répondre à un quiz de programmation en ligne.

[](https://github.com/FOSSEE/online_test#features)Caractéristiques
------------------------------------------------------------------

* Définissez des problèmes de programmation assez compliqués et demandez aux utilisateurs de résoudre le problème.
* Vérification immédiate de la solution de code.
* Prend en charge des questions de codage à peu près arbitraires en Python, C, C++, Java, R, Scilab et Bash.
* Prend en charge les choix multiples, remplissez les blancs, organisez les options et les questions basées sur le téléchargement de fichiers.
* Comme il fonctionne sur Python, vous pouvez techniquement tester n'importe quelle bibliothèque basée sur Python.
* Créez un cours avec des leçons et des quiz pour l'apprentissage en ligne.
* Surveillance presque en temps réel pour le quiz.
* Prend en charge la notation automatique et manuelle, la reclassification du quiz.
* Ajouter un système de notation au cours.
* S'adapte à plus de 500 utilisateurs simultanés.
* Distribué sous licence BSD.

Pour avoir un aperçu de toutes les fonctionnalités disponibles, consultez notre site Web de démonstration [https://yaksh-demo.fossee.in](https://yaksh-demo.fossee.in/) . Il dispose de 50 connexions d'enseignants et d'étudiants.

**Exemple de connexion enseignant**

Nom d'utilisateur : - enseignant1 Mot de passe : - enseignant1

**Exemple de connexion étudiant**

Nom d'utilisateur :- student1 Mot de passe :- student1

[](https://github.com/FOSSEE/online_test#requirements)Conditions
----------------------------------------------------------------

Python 3.6, 3.7, 3.8

Django 3.0.3

Céleri 4.4.2

[](https://github.com/FOSSEE/online_test#installation)Installation
------------------------------------------------------------------

**Remarque** : Actuellement, seuls Linux et MacOS sont pris en charge pour le projet.

Si Python 3.6 et supérieur n'est pas disponible dans le système, nous vous recommandons d'utiliser miniconda. Téléchargez miniconda avec Python 3.6 et supérieur.

**Installation de Miniconda**

1.  Téléchargez miniconda depuis [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html) selon la version du système d'exploitation.
2.  Suivez les instructions d'installation comme indiqué dans [https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation)
3.  Redémarrez le terminal.

**Prérequis**

* **Installer le serveur redis**
    
    Redis est requis pour le céleri. Celery exécute une tâche en arrière-plan pour réévaluer les soumissions.
    
    sudo apt install redis-server (Debian/Ubuntu)
     miam installer redis (Centos)
    
* **Démarrer le serveur redis**
    
    systemctl démarrer redis 
    
* **Vérifier l'état du serveur Redis**
    
    systemctl status redis 
    
* **Exécutez le travailleur du céleri**
    
    céleri -A travailleur en ligne_test -B 
    
* Assurez-vous que le [pip](https://pip.pypa.io/en/latest/installing.html) est installé
    

**Installation de Yaksh**

* **Cloner le référentiel**
    
    git clone https://github.com/FOSSEE/online_test.git 
    
* **Allez dans le répertoire online_test**
    
    cd en ligne_test 
    
* **Installez les dépendances** :
    
    * Installer Django et ses dépendances
        
        pip3 install -r requirements/requirements-common.txt 
        
    * Installer les dépendances du serveur de code
        
        sudo pip3 install -r requirements/requirements-codeserver.txt 
        

### [](https://github.com/FOSSEE/online_test#quick-start)Démarrage rapide

1.  Démarrez le serveur de code qui exécute le code utilisateur en toute sécurité :
    
    * Pour exécuter le serveur de code dans un environnement docker en bac à sable, exécutez la commande :
        
        $ invoque le démarrage 
        
    * Assurez-vous que Docker est installé sur votre système au préalable. [Installation du Docker](https://docs.docker.com/engine/installation/#desktop)
        
    * Pour exécuter le serveur de code sans docker, utilisez localement :
        
        $ invoquer start --unsafe 
        
    * Notez que cette commande exécutera le serveur de code yaksh localement sur votre machine et est sensible au code malveillant. Vous devrez installer les exigences du serveur de code en mode sudo.
        
2.  Sur un autre terminal, lancez l'application à l'aide de la commande suivante :
    
    $ invoquer le service 
    
    * _Remarque :_ La commande serve exécutera le serveur d'applications django sur le port 8000 et, par conséquent, ce port ne sera pas disponible pour les autres processus.
3.  Ouvrez votre navigateur et ouvrez l'URL`http://localhost:8000/exam`
    
4.  Connectez-vous en tant qu'enseignant pour modifier le quiz ou en tant qu'étudiant pour répondre au quiz
    
    * Étudiant - Nom d'utilisateur : étudiant | Mot de passe : étudiant
    * Enseignant - Nom d'utilisateur : enseignant | Mot de passe : enseignant
5.  L'utilisateur peut également se connecter à l'administrateur par défaut de Django en utilisant ;
    
    * Admin - Nom d'utilisateur : admin | Mot de passe : administrateur

[](https://github.com/FOSSEE/online_test#history)Histoire
---------------------------------------------------------

Chez FOSSEE, Nishanth avait mis en place une belle application basée sur Django pour tester les questions à choix multiples. Prabhu Ramachandran a été inspiré par un concours de programmation qu'il a vu à PyCon APAC 2011. Chris Boesch, qui a administré le concours, a utilisé une belle application Web [Singpath](http://singpath.com/) qu'il avait construite sur GAE qui vérifiait essentiellement votre code Python, en direct. Cela l'a rendu amusant et intéressant.

Prabhu voulait une implémentation qui n'était pas liée à GAE et a donc écrit la coupe initiale de ce qui est maintenant « Yaksh ». L'idée étant que n'importe qui peut l'utiliser pour tester les compétences de programmation des étudiants et ne pas avoir à se soucier de noter leurs réponses manuellement et le faire à la place sur leurs machines.

L'application a depuis été remaniée et maintenue par les développeurs FOSSEE.

[](https://github.com/FOSSEE/online_test#contact)Contact
--------------------------------------------------------

Pour plus d'informations et d'assistance, vous pouvez contacter

Équipe Python de FOSSEE : [pythonsupport@fossee.in](mailto:pythonsupport@fossee.in)

[](https://github.com/FOSSEE/online_test#license)Licence
--------------------------------------------------------

Celui-ci est distribué selon les termes de la licence BSD. Les informations sur les droits d'auteur se trouvent au bas de ce fichier.

[](https://github.com/FOSSEE/online_test#authors)Auteurs
--------------------------------------------------------

[Développeurs FOSSEE](https://github.com/FOSSEE/online_test/graphs/contributors)

Copyright (c) 2011-2017 [FOSSEE](https://fossee.in/)
