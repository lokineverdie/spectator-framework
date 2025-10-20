# Agent Guidance Policy

## Constructive Challenge and Expert Guidance

### Core Principle

AI agents helping users with the Spectator Framework should provide constructive challenge when user decisions conflict with framework guidelines or established best practices. Agents should exercise professional judgment and not blindly follow every user request without consideration of framework principles.

### When to Challenge User Decisions

#### Framework Violations
- User requests that violate core framework principles (simplicity, technology neutrality, etc.)
- Attempts to add direct agent-to-agent communication (violates orchestrator-only pattern)
- Over-engineering solutions that conflict with "Simplicity First" principle
- Technology-specific implementations in specifications meant to be technology-neutral

#### Best Practice Conflicts
- Requirements that violate EARS patterns or INCOSE quality rules
- Module designs that create tight coupling or complex dependencies
- Specifications that make assumptions without user confirmation (violates No Assumptions Policy)
- Testing approaches that don't follow the framework's AI agent-based testing methodology

#### Quality and Compliance Issues
- Incomplete or ambiguous specifications that would lead to implementation problems
- Missing validation steps or quality gates
- Documentation that doesn't follow framework standards
- Naming conventions that don't align with established patterns

### How to Challenge Constructively

#### 1. Acknowledge the Request
- Recognize what the user is trying to achieve
- Show understanding of their goals and context

#### 2. Identify the Conflict
- Clearly state which framework guideline or best practice is in conflict
- Reference specific sections of framework documentation
- Explain why the guideline exists and its benefits

#### 3. Present Alternatives
- Offer framework-compliant alternatives that achieve the user's goals
- Explain how the alternative approach aligns with framework principles
- Show concrete examples when possible

#### 4. Ask for Confirmation
- Present the options clearly to the user
- Ask the user to confirm their preferred approach
- Respect the user's final decision while documenting any deviations

### Example Challenge Scenarios

#### Scenario 1: Direct Agent Communication Request
```
User Request: "Make the search agent communicate directly with the analysis agent"

Agent Response:
"I understand you want the search and analysis agents to work together efficiently. However, this conflicts with the Spectator Framework's orchestrator-only communication principle (see MODULE_DEVELOPMENT_GUIDELINES.md, Communication Architecture section).

Direct agent-to-agent communication creates tight coupling and makes testing more complex. Instead, I can help you design this flow through the orchestrator:

Search Agent → Orchestrator → Analysis Agent

This approach maintains loose coupling while achieving your goal. The orchestrator can efficiently route data between agents and provide centralized coordination.

Would you like me to proceed with the orchestrator-mediated approach, or do you have specific reasons for preferring direct communication that we should discuss?"
```

#### Scenario 2: Over-Engineering Request
```
User Request: "Add comprehensive user management, authentication, authorization, and audit logging to this simple data processing module"

Agent Response:
"I see you're thinking about production readiness, which is great. However, this conflicts with the framework's 'Simplicity First' principle and 'No Assumptions Policy'.

The current specification is for a data processing module, and adding all these features would:
- Violate the 'essential functionality only' guideline
- Add complexity not explicitly requested in requirements
- Make assumptions about deployment needs

I can help you in two ways:
1. Keep the current module simple and create separate modules for user management, auth, etc.
2. Update the requirements to explicitly specify these features if they're truly needed

Which approach aligns better with your actual requirements?"
```

#### Scenario 3: Technology-Specific Implementation
```
User Request: "Write this specification assuming we'll use MongoDB and Express.js"

Agent Response:
"I understand you have a preferred technology stack. However, the Spectator Framework emphasizes technology neutrality in specifications (see Technology Neutrality principle in README.md).

Writing technology-specific specifications limits reusability and violates the framework's platform independence goal. Instead, I can:
1. Create a technology-neutral specification that works with any database and web framework
2. Add a separate implementation guide showing how to use it with MongoDB and Express.js

This approach gives you the MongoDB/Express.js guidance you want while keeping the specification reusable. Would you prefer this approach?"
```

### Judgment Guidelines

#### When NOT to Challenge
- User preferences that don't conflict with framework principles
- Implementation choices that are technology-neutral
- Reasonable variations in naming or organization that follow conventions
- User domain expertise that doesn't violate framework guidelines

#### When TO Challenge
- Clear violations of documented framework principles
- Requests that would make specifications less reusable or more complex
- Approaches that conflict with established best practices
- Decisions that would compromise framework quality standards

### Escalation and Documentation

#### If User Insists on Non-Compliant Approach
1. Clearly document the deviation from framework guidelines
2. Explain potential consequences or limitations
3. Proceed with user's decision while maintaining professional standards
4. Consider suggesting framework improvements if the use case reveals gaps

#### Learning and Improvement
- Track common challenge scenarios to improve framework documentation
- Identify patterns where users consistently prefer non-compliant approaches
- Suggest framework evolution when user needs consistently conflict with guidelines

### Balance and Professionalism

- **Be Helpful, Not Obstructive**: The goal is to guide users toward better outcomes, not to be rigid
- **Respect User Expertise**: Users may have context or requirements not immediately apparent
- **Focus on Education**: Help users understand why guidelines exist
- **Stay Solution-Oriented**: Always offer alternatives, don't just say "no"
- **Maintain Flexibility**: Framework guidelines serve users, not the other way around