# rendu-django

## Stack
- django-bootstrap-v5 
- db sqlite
- template html css (theme)
- swiperjs

## Sections

### Home
- Layout base qui contient la navbar
- Gestion de l'authentification

### Nos projets
- Blog permettant aux utilisateurs de faire des posts (titre, texte et image)
- Gestion des permissions. Le staff peut publier ou archiver des posts.
- Les utilisateurs doivent attendre que leur post soit validé et publié par le staff pour qu'il soit visible pour tous

### Candidature
- Les utilisateurs peuvent poster des candidatures (titre du post, description, CV)
- Les recruteurs qui font partie du groupe "staff" peuvent voir toutes les candidatures
- Les utilisateurs ne peuvent voir que leurs candidatures

## Routes
- ``'/'`` : Home
- ``'/projets'`` : Nos projets
- ``'/candidature'`` : Candidature

## Groupe
- Valentin Kahn
- Jeremy Blahak
- Jordan Sinou
