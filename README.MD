Questo è un convertitore creato in mezz'ora per rendere i file Markdown leggibili dal sito in Jekyll https://theromanxpl0.it/

L'unica differenza che ho trovato tra i file Markdown normali e quelli accettati da Jekyll sta nelle immagini.

Markdown:
`![Example of using various methods to send information to the server](./media/img/body_params.png)`

Jekyll:
`<img class="img-responsive" src="{{ site-url }}/assets/openecsc2024/Perfect-Shop/img/body_params.png" alt="Example of using various methods to send information to the server">` 

ovvero come fosse codice HTML.

Quello che fa questo converter è leggere il campo `title` e `categories` di un post/writeup cercando di convertire le immagini da Markdown ad HTML con un path consono.

L'esempio riportato di sopra è stato ricostruito con l'aiuto dei seguenti metadati:
```m
layout: post
title: OpenECSC 2024 - Perfect Shop
categories: ctf_openecsc2024
keywords: "web"
comments: true
authors:
    - Tiziano-Caruana
```

Il risultato è `<img class="img-responsive" src="{{ site-url }}/assets/[CTF]/[challenge]/[path]" alt="[alt del markdown]">`

Dove CTF è il valore di `categories` troncato prima del `ctf_` compreso, challenge è il valore di `title` troncato prima del `- ` e con gli spazi sostituiti da `-`, e il path preso dal markdown a partire dal penultimo `/`.