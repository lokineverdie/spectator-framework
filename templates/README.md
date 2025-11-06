# Spectator Framework Templates

Simple, ready-to-use templates following the framework's "simplicity first" principle.

## Available Templates

### Spec Template (`specs/`)
For creating Kiro specification workflows:
- **requirements.md**: EARS-compliant requirements template
- **design.md**: Technology-neutral design template
- **tasks.md**: Implementation planning template

### Module Template (`module-template/`)
For creating agent modules:
- **README.md**: Usage instructions and customization guide
- **architecture.puml**: Simple architecture diagram
- **data-models.puml**: Data structure definitions
- **agent-prompts.xml**: Agent behavior definitions

## Quick Start

### Create a New Specification
```bash
# Copy spec template
cp -r templates/specs .kiro/specs/your-feature-name

# Fill out the files:
# 1. requirements.md - What should the system do? (EARS patterns)
# 2. design.md - How should it work? (technology-neutral)
# 3. tasks.md - Implementation steps
```

### Create a New Module
```bash
# Copy module template
cp -r templates/module-template modules/your-module-name

# Customize the files:
# - Replace {MODULE_NAME} with your module name
# - Update architecture.puml for your design
# - Modify data-models.puml for your data
# - Customize agent-prompts.xml for your agent
```

## Template Principles

- **Simplicity First**: Minimal viable templates with essential elements only
- **Technology Neutral**: Work with any implementation platform
- **Framework Compliant**: Follow orchestrator-only communication and EARS patterns
- **Easy to Customize**: Clear placeholders and examples
- **Cache Optimized**: Structured for maximum prompt caching efficiency

## Customization Process

1. **Copy template** to your target location
2. **Replace placeholders** systematically:
   - `{MODULE_NAME}` → Your module name
   - `{AGENT_NAME}` → Your agent name  
   - `{DOMAIN}` → Your domain area
3. **Update content** for your specific use case
4. **Validate** PlantUML syntax and XML format
5. **Test** against framework compliance

## Getting Help

- Each template includes detailed README with usage instructions
- Check `FRAMEWORK_CORE.md` for core principles
- Review `DEVELOPMENT_GUIDE.md` for development practices
- See main README.md for framework overview