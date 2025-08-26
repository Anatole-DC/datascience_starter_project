# Continuous Integration & Continuous Delivery (CI/CD)

CI-CD are pipelines that automate tasks performed against your code like :
- check your code quality (with linters)
- run tests
- build your package
- deploy your code

```{admonition} Work in progress !
:class: warning

If you want to find out more about this subject before the section is updated, contact-me.
```

## Tools

They are many CI-CD tools that all come with there advantages and weaknesses :
- Github actions
  + **\+** Integrated with github
  + **\+** Customizable
  + **\-** No the most user friendly
- Gitlab CI
  + **\+** Integrated with gitlab
  + **\+** Unlimitted power when self hosted
  + **\-** Made for one ci file in project (you have to know your yaml)
- CircleCI
  + **\+** User friendly
  + **\-** Limitted in usage (unless you pay)
- Jenkins (Never used it)
  + **\+** Fully self hosted
  + **\-** Kinda old

Most of them use [yaml](https://yaml.org/) to configure the pipelines. They all offer similar features :
- Usage of container for your pipeline stages to run on appropriate architecture
- The integrate Docker well
- Provide cache and artifacts registry

```{admonition} Controversial opinion
:class: danger

CI-CD config files are one of the most appropriate task Generative AI usage. They are actually really good at it, and it saves you ton of time.

The prompt usually :
- Specify which ci-cd tool I am using
- Indicates the project stack :
  - Language
  - Tools used for testing
  - Purpose of the project
- Asks a config for the steps and the order of steps (usually in this order)
  - Linting
  - Testing
  - Build
  - Package
  - Deploy package
  - Deploy app
```
