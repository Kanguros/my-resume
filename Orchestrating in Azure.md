## Orchestrating in Azure

An idea to use Azure Devops (mainly) services in order to deliver workflow solution. 

---

### Requirements

-   Workflow could be run:
    -   on demand
    -   on time
    -   by external trigger 
-   Easy to maintain 
-   Being able to share Actions across workflows.

### On demand

Quite easy. A Azure Pipeline could be executed at any time, by someone with right privileges to do so (no idea which ones). 

It also could take parameters. Which are more capable of storing complex data than variables (source required)

### On time

Executed based on date and/or time. 

As far as I know, a Azure Pipeline has a keyword in its syntax to define a `schedule` or something. To be verified. 

### By external trigger 

Being able to shoot to Azure API and execute a desire Azure Pipeline. It should be able to pass parameters. 

## How to define a workflow?

-   Should all *Workflow's* structure should be the same? Follow the same schema?
    -   How it should look like?

**I see one obstacle.** 

A Azure Pipeline could take any numbers of defined parameters. 

1.   Single Azure Pipeline would be a single Workflow but with named parameters.
2.   Pipeline could take a Workflow name as a parameter but than it would be hard to defined common parameters for all Workflows inside. Or it could accept kwargs. But it less straightforword.

To find out during testing. Maybe there will be a possibility to run different Azure Pipelines from single Repo. 

## Ideas for implementation



-   



## Example workflow

Its more like pseudo than code.

```
Pipeline executed by {source}
?
```

## Security

All connections should be made from defined, not shared with anyone else *Agent Pool*



## Unrelated notes

-   All passwords or other critical data could be obtained from Azure Key Vault.

-   An Ansible could be used.
-   Python's `invoke`