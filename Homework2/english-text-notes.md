## Agile Model Driven Development (AMDD): The Key to Scaling Agile Software Development

### Overview

- AMDD -> agile model driven development
- MDA -> model driven architecture (by Object Management Group OMG)
- less models with AMDD, barely enough to keep implementation going
- iteration 0 = inception; iteration = sprint / cycle
- envisioning = intial requirements envisioning + initial architecture envisioning

### Envisioning

- mainly to gain an idea of what the project is all about, not for extensive docummentation
- usually during 1 week of a project
- longer envisioning is risky, no feedback from implementation
- high level requirements modeling + architecture modeling
- initial reaquirements modelling
  - define scope of 1 iteration
  - usage model required to see how users will interact with the system
  - initial domain model to identify buisness entity types & relationships between them
  - initial user inteface model -> UI & usability issues
- initial architecture modelling
  - set a technical direction and organize team
  - something just barely good enough, will evolve
  - whiteboard sketch of architecture is good enough, points list for use-case also

### Iteration Modeling

- most important tasks (by priority) are placed on top of the stack
- based on team velocity, enough tasks are picked off the stack to be completed during the 
iteration
- modelling to discuss with team how long each requirement would take to implement to better 
judge work (analysis and design of requirements)

### Model Storming

- 5 to 10 minutes usually, rearely over  30
- team member asks another to model storm something
- JIT (just in time modeling), usually right before coding
- called stand-up-design by extreme programmers
- issue comes up and needs quick resolving, team members ask each other for help

### Executable Specification via Test Driven Developments

- test driven design (TDD) = test first design (TFD) + refactoring
- majority of detailed modeling done in the form of executable specifications (often customer / 
development tests)
- refactoring -> evolve design in small steps to ensure work remains of high quality
- AMDD provides high-level specification; TDD not so much
- modeling tools can increase team productivity, require greater modeling skillset

### Reviews

- model reviews & code inspections obsolete in agile development
- very helpful on larger teams and complex situations

### How is AMDD Different

- less modeling
- more coding
- iterate back to models when needed
- different form feature driven development (FDD) & use case driven development (UCDD) as it 
does not specify the models to be created
- best model for current case is choosen, team is free to decide what is most needed
- no modeling specialists needed, instead overall speacialists

### Why does it work?

- project planning needs can be met good enoguh with early modeling 
- technical risk managed by reducing over modeling and creating models when enough knowledge is 
gathered
- minimize wastage -> models are not thrown in the bin, they always work out
- aks better questions -> more knowledge gathered when modeling
- Stakeholders give better answers 

### Approaches to AMDD

- manual & simple tools -> whiteboard; 70-80%
- Design Tool & Inclusive models -> explore requirements with stakeholders & analyze 
requirements; 20-30%
- Agile MDA -> extensive models from which sotware is generated; 5-10%
