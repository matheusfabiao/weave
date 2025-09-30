# **Sobre o Projeto Weave**

O Weave nasce da ideia de construir um sistema simples mas eficiente que utilize três dos bancos de dados mais populares atualmente: o `PostgreSQL`, `Redis` e o `Firebase Database`, banco de dados em nuvem mantido pelo Google. A seguir, desvendaremos o papel que cada um deles neste projeto.

## PostgreSQL

Um dos bancos de dados mais famosos da atualidade, mais especificamente o 4º lugar no ranking segundo a **[DB Engines](https://db-engines.com/en/ranking)**, é responsável por manter os dados dos usuários da aplicação, bem como os artigos escritos pelos usuários e as tags (palavras-chave) usadas em cada um desses artigos. Sua escolha se deve pela facilidade de integração com o ecossistema Django e por sua robustez, sendo capaz de suportar inúmeras tabelas e tuplas, tornando-se extremamente importante quando pensamos no longo prazo da aplicação.

![postgres](assets/PostgreSQL-Logo.jpg){ width="300" }

## Redis

É um repositório de dados NoSQL em memória amplamente reconhecido por sua flexibilidade no quesito de aplicabilidade, uma vez que pode ser utilizado como banco de dados, cache, gerenciador de filas e sessões, mensageiro, etc. Seu armazenamento funciona no modelo chave-valor, no qual cada dado é associado a uma chave única. No projeto Weave, usamos o Redis como cache, com o Django armazenando dados de _queries_ e até mesmo páginas inteiras que não mudam com frequência na memória RAM, permitindo que a aplicação ganhe bastante desempenho durante seu tempo de execução.

![redis](assets/redis-logo-database-mongodb-gearman-png-favpng-Q3Z0HRK11yc0H8hG4RYEtTfpV.jpg){ width="300" }

## Firebase Database

O Google possui uma plataforma voltada para o desenvolvimento de aplicativos chamada `Firebase`, no qual oferece diversos serviços úteis para auxiliar os desenvolvedores na construção desses aplicativos. Um desses serviços é o `Firebase Database`, que possui "uma variante" assíncrona: o `Firebase Real Time Database`. O projeto utiliza tal variante, mas para fins de estudo, não executamos nenhuma operação em tempo real, então poderíamos tranquilamente usar o "banco de dados tradicional" do Firebase.

![firebase](assets/New_Firebase_logo.svg.png){ width="300" }

Sua utilidade se deu por conta das interações dos usuários com as publicações, ou seja, cada `like` e `comentário` computado em nossa rede social ficará armazenada e disponível para consulta dentro do banco do Firebase. Além disso, temos uma funcionalidade de `trending`, que traduzindo para termos simples significa os posts com o maior engajamento (maior número de curtidas e comentários), no qual os dados são lidos diretamente do Firebase e o Django é o responsável por realizar os cálculos e atualizar o ranking dos artigos mais engajados e disponibilizar a informação para os usuários.