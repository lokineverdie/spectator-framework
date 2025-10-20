# Naming Conventions

This document defines standardized naming patterns for all artifacts in the job search assistant template framework.

## Directory Naming

### Primary Directories
- `modules/` - Individual module specifications and templates
- `templates/` - Reusable documentation and code templates
- `data-models/` - PlantUML class diagram definitions
- `diagrams/` - Architecture and workflow visualizations
- `examples/` - Reference implementations and samples

### Module Directories
- Use **kebab-case** for all module names (e.g., `web-search`, `resume-analysis`)
- Include version subdirectories when needed: `{module-name}/v1.0/`
- Maintain consistent internal structure across all modules

### Subdirectory Structure
```
{module-name}/
├── diagrams/           # PlantUML architecture diagrams
├── data-models/        # PlantUML class diagram definitions
└── prompts/           # XML agent prompt templates
```

## File Naming

### Documentation Files
- `requirements.md` - Module requirements following EARS patterns
- `design.md` - Architecture and component specifications
- `tasks.md` - Implementation planning and task breakdown
- `README.md` - Directory overview and usage guidelines

### Diagram Files
- `architecture.puml` - Module internal architecture
- `workflows.puml` - Process flow diagrams
- `integration.puml` - Inter-module communication patterns
- Use descriptive prefixes: `{module-name}-architecture.puml`

### Data Model Files
- `data-models.puml` - Combined data model class diagrams
- `{entity-name}-model.puml` - Individual entity class definitions
- `config-model.puml` - Configuration parameter class definitions
- `interface-model.puml` - Module communication interface definitions

### Template Files
- `{type}-template.{ext}` - Reusable templates (e.g., `requirements-template.md`)
- `{module-type}-template.{ext}` - Module-specific templates
- Include version in filename when needed: `template-v2.md`

### Prompt Files
- `agent-prompts.xml` - Combined agent prompt definitions
- `{agent-type}-prompts.xml` - Agent-specific prompts
- `conversation-flows.xml` - Interaction pattern definitions

## Identifier Naming

### Module Identifiers
- Format: `{category}-{function}` (e.g., `search-jobs`, `analyze-resume`)
- Categories: `search`, `analyze`, `communicate`, `track`, `orchestrate`
- Use present tense verbs for functions

### Class Identifiers
- Use **PascalCase** for class names (e.g., `UserProfile`, `JobPosting`)
- Use **camelCase** for property names (e.g., `firstName`, `jobTitle`)
- Include namespace prefixes when needed: `JobSearch.UserProfile`

### Agent Identifiers
- Format: `{Domain}Agent` (e.g., `SearchAgent`, `AnalysisAgent`)
- Use descriptive domain names that clearly indicate responsibility
- Maintain consistency with module categories

## Version Control Patterns

### Branch Naming
- `feature/{module-name}-{feature}` - New module development
- `update/{module-name}-{change}` - Module modifications
- `template/{template-type}` - Template updates
- `framework/{component}` - Framework-level changes

### Tag Naming
- `v{major}.{minor}.{patch}` - Framework versions (e.g., `v1.0.0`)
- `{module-name}-v{version}` - Module-specific versions
- `template-v{version}` - Template releases

### Commit Message Format
```
{type}({scope}): {description}

Types: feat, fix, docs, style, refactor, test, chore
Scopes: framework, module, template, data-model, example
```

## Quality Standards

### Consistency Rules
- All names must be descriptive and self-documenting
- Avoid abbreviations unless they are widely understood
- Use consistent terminology across all artifacts
- Maintain alignment with glossary definitions

### Validation
- Names must not contain spaces or special characters (except hyphens and underscores)
- Directory names must be lowercase with hyphens
- File names must follow established patterns
- Class identifiers must follow PlantUML naming conventions

### Documentation
- Include naming rationale in module documentation
- Update conventions when patterns evolve
- Provide examples for each naming category
- Maintain cross-reference with framework glossary