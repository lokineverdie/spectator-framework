# Spectator Framework

A simple framework for creating system-agnostic agent specifications through spec-driven development.

## What Is This?

Spectator Framework helps you build technology-neutral agent specifications that work across any platform. Instead of being locked into specific technologies, you create specifications first, then choose implementation technologies later.

## Core Concepts

### Multi-Agent Architecture
- **Orchestrator Agent**: Coordinates all workflow and agent communication
- **Specialized Agents**: Handle specific tasks (search, analysis, communication, etc.)
- **Hub-and-Spoke Communication**: Agents only talk to orchestrator, never directly to each other

### Spec-Driven Development
1. Write specifications using EARS patterns
2. Create technology-neutral designs
3. Generate implementation tasks
4. Choose technologies during implementation

### Key Principles
- **Simplicity First**: Only add complexity when needed
- **Technology Neutral**: Specifications work with any tech stack
- **No Assumptions**: Implement only what's explicitly specified
- **Modular Design**: Independent, testable components

## Quick Start

### 1. Create a New Specification
```bash
# Copy the spec template
cp -r templates/spec-template .kiro/specs/your-feature-name

# Fill out the files:
# 1. requirements.md - What the system should do (EARS patterns)
# 2. design.md - How it should work (technology-neutral)
# 3. tasks.md - Implementation steps
```

### 2. Create a New Module
```bash
# Copy the module template
cp -r templates/module-template modules/your-module-name

# Customize the files:
# - Replace placeholders with your module name
# - Update architecture.puml for your design
# - Modify data-models.puml for your data
# - Customize agent-prompts.xml for your agent behavior
```

### 3. Follow the Framework Rules
- Read `FRAMEWORK_CORE.md` for core principles
- Check `DEVELOPMENT_GUIDE.md` for development practices
- Use EARS patterns for requirements
- Keep orchestrator-only communication

### 4. Advanced: Build Modular Prompts (Optional)
For complex agents, use modular prompt development:
```bash
# Build a modular prompt from components
python build-modular-prompt.py your-agent-name --validate

# This combines prompt-parts/*.xml files into a final agent prompt
```

## File Structure

```
spectator-framework/
├── templates/                # Ready-to-use templates
├── modules/                  # Your created modules (when you make them)
├── README.md                 # This file
├── FRAMEWORK_CORE.md         # Core principles and architecture
├── DEVELOPMENT_GUIDE.md      # Development practices and guidelines
├── CONTRIBUTING.md           # How to contribute
└── build-modular-prompt.py   # Modular prompt builder tool
```

## Templates Available

### Spec Template (`templates/spec-template/`)
- **requirements.md**: EARS-compliant requirements template
- **design.md**: Technology-neutral design template  
- **tasks.md**: Implementation planning template

### Module Template (`templates/module-template/`)
- **README.md**: Usage instructions and customization guide
- **architecture.puml**: Simple architecture diagram
- **data-models.puml**: Data structure definitions
- **agent-prompts.xml**: Agent behavior definitions

### Modular Prompt Builder (`build-modular-prompt.py`)
For complex agents, build prompts from modular components:
- Break down complex prompts into focused, reusable components
- Maintain consistency across agents with shared components
- Optimize for prompt caching by separating static and dynamic content

### Prompt Optimization Guide (`PROMPT_OPTIMIZATION_GUIDE.md`)
Comprehensive best practices for major LLM providers:
- Minimize tokens while maintaining performance
- Maximize cache hit rates (up to 90% cost reduction)
- Provider-specific optimization for OpenAI, Claude, and Meta models

## Example Workflow

1. **Start with a user story**: "As a user, I want to search for jobs"
2. **Create requirements**: Use EARS patterns to specify what the system should do
3. **Design the solution**: Create technology-neutral architecture
4. **Plan implementation**: Break down into actionable tasks
5. **Choose technologies**: Select appropriate tools for your environment
6. **Build and test**: Implement following the specifications

## Getting Help

- Check `FRAMEWORK_CORE.md` for core principles
- Review `DEVELOPMENT_GUIDE.md` for development practices
- Look at template README files for usage instructions
- See `CONTRIBUTING.md` for contribution guidelines

## Benefits

- **Technology Freedom**: Choose the best tools for your situation
- **Clear Requirements**: Well-defined specifications reduce confusion
- **Modular Design**: Build and test components independently
- **Consistent Standards**: Unified approach across projects
- **Reduced Assumptions**: Clear boundaries prevent over-engineering