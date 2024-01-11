# PythonBookStore

O projeto em questão representa um sistema de biblioteca, construído sobre a arquitetura n-layer, com ênfase no desenvolvimento em Python e integração eficaz com diversos serviços da AWS. Trata-se de uma aplicação de gerenciamento, seguindo a lógica do CRUD (Create, Read, Update, Delete).

## Arquitetura

A arquitetura do projeto segue o padrão de camadas (n-layer), dividindo a aplicação em componentes distintos para facilitar a manutenção e escalabilidade.


![N-Layer](https://github.com/Jokebede-Coimbra/ProjetoPythonBookStore/assets/44805096/7a1aec09-8b32-4aed-a6b5-0a4ca027c237)

### Tecnologias e Serviços AWS Utilizados:
<p float="left">
<img align="center" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" alt="python" style="max-width:100%">
<img align="center" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" alt="flask" style="max-width:100%">
<img align="center" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original.svg" alt="AWS" style="max-width:100%">
<img align="center" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-plain.svg" alt="docker" style="max-width:100%">
</p>

![CrudProject](https://github.com/Jokebede-Coimbra/ProjetoPythonBookStore/assets/44805096/d4b8436c-795a-43a7-8d85-91b3937b41df)


**Amazon S3 (Simple Storage Service):**

*O Amazon S3 foi utilizado como serviço de armazenamento de objetos para hospedar e gerenciar imagens relacionadas ao projeto. Essa escolha permite o armazenamento seguro, escalável e altamente disponível de recursos visuais, melhorando o desempenho da aplicação.*

**Amazon API Gateway:**

*O Amazon API Gateway desempenha um papel central na exposição e gerenciamento de APIs. Foi implementado para facilitar a comunicação entre os serviços, oferecendo uma interface unificada para a integração eficiente entre os diferentes componentes do sistema.*

**Elastic Load Balancing:**

*O serviço de Elastic Load Balancing foi adotado para distribuir o tráfego de forma equilibrada entre as instâncias do Amazon ECS/Fargate. Isso assegura alta disponibilidade, escalabilidade e resiliência, melhorando a performance da aplicação.*

**Amazon ECS/Fargate:**

*Amazon ECS (Elastic Container Service) em conjunto com o serviço Fargate foram escolhidos para orquestrar e gerenciar os contêineres que executam a aplicação. Isso proporciona uma abordagem altamente escalável e flexível para a implementação e execução de containers, simplificando a infraestrutura.*

**Amazon DynamoDB:**

*O Amazon DynamoDB foi selecionado como banco de dados NoSQL para armazenar dados relacionados ao projeto. Sua escalabilidade automática e desempenho rápido tornam-no uma escolha eficiente para armazenamento e recuperação de dados.*

**AWS Lambda:**

*O AWS Lambda é utilizado para a execução de funções serverless, proporcionando uma abordagem eficiente para execução de código sem a necessidade de gerenciamento de servidores. Sua aplicação no projeto contribui para a escalabilidade e eficiência na execução de tarefas específicas.*

**Docker:**

*O Docker desempenha um papel essencial no processo, possibilitando a criação eficiente da imagem contendo todos os componentes necessários. Essa imagem é então implantada de maneira eficaz no Amazon ECS/Fargate, proporcionando uma abordagem padronizada e eficiente para a gestão de contêineres.*

**Python**

*É o backend principal da minha aplicação, feita em Python para ter experiência com o ecossistema python, garanto uma experiência rica e consistente.*

**Flask**

*O backend principal da minha aplicação é desenvolvido em Python, com especial destaque para o uso do framework Flask para a implementação da funcionalidade de leitura (read) no CRUD. Ao escolher Flask, busquei uma abordagem leve e eficiente para lidar com as operações de consulta, aproveitando a simplicidade e flexibilidade oferecidas por este framework.*



## Contribuição

Jefté : https://github.com/jeftegoes


## Extra > Frontend
https://github.com/Jokebede-Coimbra/AngularBookStoreCRUD


