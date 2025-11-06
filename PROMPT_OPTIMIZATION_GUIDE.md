# Prompt Optimization Guide for Major LLM Providers

## Overview

This guide provides comprehensive best practices for optimizing prompts across major LLM providers to minimize tokens, maximize cache hit rates, and maintain performance and consistency.

## OpenAI Models (GPT-4, GPT-4o, GPT-3.5)

### Prompt Caching (GPT-4o and newer)

#### Cache Requirements
- **Minimum tokens**: 1024+ tokens required for cache activation
- **Cache increments**: Works in 128-token increments (1024, 1152, 1280, etc.)
- **Automatic activation**: No special configuration needed
- **Prefix matching**: Cache hits require exact prefix matches
- **Rate limits**: Stay under 15 requests/minute per prefix for optimal caching

#### Optimization Strategies
```
# OPTIMAL STRUCTURE FOR CACHING
[STATIC CONTENT - CACHED]
System instructions (detailed role definition)
Tool definitions and schemas
Examples and templates
Context that rarely changes
Knowledge base information

[VARIABLE CONTENT - NOT CACHED]
User input
Session-specific data
Dynamic parameters
Request timestamps
```

#### Token Minimization Techniques
1. **Concise System Messages**
   - Use bullet points instead of paragraphs
   - Eliminate redundant phrases
   - Use abbreviations for repeated concepts

2. **Efficient Tool Definitions**
   - Minimize parameter descriptions
   - Use JSON schema efficiently
   - Group related parameters

3. **Smart Example Selection**
   - Use 2-3 high-quality examples instead of many
   - Choose examples that cover edge cases
   - Keep examples concise but complete

### Performance Optimization

#### Response Consistency
- Use temperature 0.1-0.3 for consistent outputs
- Set max_tokens to prevent runaway responses
- Use stop sequences for structured outputs

#### Structured Output Techniques
```json
{
  "response_format": {
    "type": "json_object"
  },
  "messages": [
    {
      "role": "system",
      "content": "Always respond with valid JSON matching this schema: {...}"
    }
  ]
}
```

## Claude Models (Opus, Sonnet, Haiku)

### Prompt Caching

#### Cache Requirements
- **Minimum tokens**: 
  - Claude 3.5 Sonnet: 1024 tokens
  - Claude 3.5 Haiku: 4096 tokens
  - Claude 3 Opus/Sonnet: 1024 tokens
  - Claude 3 Haiku: 2048 tokens
- **Cache control**: Use `cache_control: {"type": "ephemeral"}` parameter
- **Cache hierarchy**: Tools → System → Messages (in that order)
- **TTL options**: 5 minutes (default) or 1 hour (`"ttl": "1h"`)

#### Optimization Structure
```json
{
  "system": [
    {
      "type": "text",
      "text": "Static system instructions...",
      "cache_control": {"type": "ephemeral"}
    },
    {
      "type": "text",
      "text": "Additional context or examples...",
      "cache_control": {"type": "ephemeral"}
    }
  ],
  "tools": [
    {
      "name": "tool_name",
      "description": "Tool description",
      "input_schema": {...},
      "cache_control": {"type": "ephemeral"}
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": "Variable user input..."
    }
  ]
}
```

#### Advanced Caching Strategies
1. **Hierarchical Caching**
   - Cache tools first (most stable)
   - Cache system instructions second
   - Keep messages dynamic

2. **Cache Block Optimization**
   - Place cache control on the last block of static content
   - Use automatic prefix checking (up to 20 blocks)
   - Consider 1-hour cache for recurring but infrequent requests

### Token Minimization for Claude

#### Efficient Prompt Structure
- Use XML tags for clear structure: `<instructions>`, `<examples>`, `<context>`
- Leverage Claude's strong instruction following to reduce verbose explanations
- Use thinking tags `<thinking>` for complex reasoning (not counted in output)

#### Example Optimized Structure
```xml
<instructions>
You are a {role}. Follow these rules:
- Rule 1: Brief description
- Rule 2: Brief description
- Rule 3: Brief description
</instructions>

<examples>
<example>
Input: {input}
Output: {output}
</example>
</examples>

<context>
{dynamic_context}
</context>
```

## Meta Models (Llama 2, Llama 3, Code Llama)

### Optimization for Open Source Models

#### Prompt Structure Best Practices
- Use clear delimiters: `###`, `---`, or `[INST]...[/INST]`
- Be explicit about format requirements
- Include system prompts in user message for older models

#### Token Efficiency
```
# EFFICIENT LLAMA PROMPT STRUCTURE
[INST] <<SYS>>
{concise_system_prompt}
<</SYS>>

{user_instruction} [/INST]
```

#### Performance Optimization
1. **Context Window Management**
   - Llama 2: 4K context (2K recommended for performance)
   - Llama 3: 8K context (6K recommended)
   - Use sliding window for long conversations

2. **Instruction Clarity**
   - Be more explicit than with commercial models
   - Use step-by-step instructions
   - Provide clear output format examples

## Universal Best Practices

### Token Minimization Strategies

#### 1. Content Optimization
- **Remove filler words**: "please", "kindly", "I would like"
- **Use abbreviations**: "e.g." instead of "for example"
- **Eliminate redundancy**: Don't repeat instructions
- **Compress examples**: Use minimal viable examples

#### 2. Structural Efficiency
```
# INEFFICIENT (verbose)
Please analyze the following data and provide a comprehensive analysis including trends, patterns, and recommendations for future actions.

# EFFICIENT (concise)
Analyze data: identify trends, patterns, recommendations.
```

#### 3. Smart Templating
- Use placeholders: `{user_input}`, `{context}`, `{timestamp}`
- Separate static from dynamic content
- Reuse common instruction blocks

### Cache Hit Rate Optimization

#### 1. Consistent Structure
- Maintain identical prompt structure across requests
- Use consistent ordering of elements
- Standardize formatting and spacing

#### 2. Strategic Content Placement
```
# OPTIMAL CACHE STRUCTURE
[STATIC - HIGH CACHE VALUE]
Role definition
Tool schemas
Examples
Business rules
Knowledge base

[SEMI-STATIC - MEDIUM CACHE VALUE]
User preferences
Session context
Recent history

[DYNAMIC - NO CACHE VALUE]
Current request
Real-time data
Timestamps
```

#### 3. Version Control for Prompts
- Use semantic versioning for prompt templates
- Track cache performance metrics
- A/B test prompt variations

### Performance and Consistency

#### 1. Response Consistency
- Use low temperature (0.1-0.3) for deterministic outputs
- Set appropriate max_tokens limits
- Use stop sequences for structured responses
- Implement retry logic with exponential backoff

#### 2. Quality Assurance
```python
# Example validation pattern
def validate_response(response, expected_schema):
    """Validate response against expected structure"""
    try:
        parsed = json.loads(response)
        # Validate against schema
        return is_valid_schema(parsed, expected_schema)
    except:
        return False
```

#### 3. Monitoring and Metrics
- Track cache hit rates
- Monitor response times
- Measure token usage
- Validate output quality

## Provider-Specific Recommendations

### OpenAI Optimization Checklist
- [ ] Prompt reaches 1024+ tokens for caching
- [ ] Static content placed at beginning
- [ ] Consistent structure maintained
- [ ] Temperature set appropriately (0.1-0.3)
- [ ] JSON mode used for structured outputs

### Claude Optimization Checklist
- [ ] Cache control blocks added to static content
- [ ] Minimum token requirements met per model
- [ ] XML structure used for clarity
- [ ] Tools cached separately from system messages
- [ ] Hierarchical caching implemented

### Meta/Llama Optimization Checklist
- [ ] Clear instruction format used
- [ ] Context window limits respected
- [ ] Explicit output format specified
- [ ] Step-by-step instructions provided
- [ ] Sliding window implemented for long contexts

## Implementation Examples

### OpenAI Optimized Prompt
```python
{
    "model": "gpt-4o",
    "temperature": 0.2,
    "max_tokens": 1000,
    "messages": [
        {
            "role": "system",
            "content": """You are a data analyst. Rules:
- Analyze data for trends and patterns
- Provide actionable insights
- Format output as JSON
- Include confidence scores

Examples:
Input: Sales data Q1-Q4
Output: {"trends": ["increasing"], "insights": ["seasonal peak Q4"], "confidence": 0.85}

Schema: {"trends": [str], "insights": [str], "confidence": float}"""
        },
        {
            "role": "user", 
            "content": f"Analyze: {user_data}"
        }
    ]
}
```

### Claude Optimized Prompt
```python
{
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 1000,
    "system": [
        {
            "type": "text",
            "text": """<instructions>
You are a data analyst. Follow these rules:
- Analyze for trends and patterns
- Provide actionable insights  
- Format as JSON with confidence scores
</instructions>

<examples>
<example>
Input: Sales data Q1-Q4
Output: {"trends": ["increasing"], "insights": ["seasonal peak Q4"], "confidence": 0.85}
</example>
</examples>""",
            "cache_control": {"type": "ephemeral"}
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": f"<data>{user_data}</data>"
        }
    ]
}
```

### Llama Optimized Prompt
```python
prompt = f"""[INST] <<SYS>>
You are a data analyst. Analyze data for trends, patterns, and insights. 
Output format: JSON with trends, insights, and confidence score.
<</SYS>>

Analyze this data and provide insights:
{user_data}

Format: {{"trends": ["trend1"], "insights": ["insight1"], "confidence": 0.85}} [/INST]"""
```

## Cost Optimization Summary

### Token Reduction Impact
- **25-40% reduction**: Removing verbose language and filler words
- **15-30% reduction**: Optimizing examples and instructions
- **10-20% reduction**: Efficient JSON schema design
- **5-15% reduction**: Smart abbreviations and formatting

### Cache Hit Rate Impact
- **80-90% cost reduction**: High cache hit rates with proper structure
- **50-70% latency reduction**: Cached responses return faster
- **Improved consistency**: Cached prompts ensure identical behavior

### ROI Calculation
```
Monthly savings = (Total tokens * Token cost * Cache hit rate * Discount rate)
Example: 10M tokens * $0.01 * 0.8 cache hit * 0.9 discount = $72,000 saved
```

This guide provides the foundation for implementing efficient, cost-effective prompts across all major LLM providers while maintaining high performance and consistency.