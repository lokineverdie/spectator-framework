# No Assumptions Policy - Agent Implementation Guidelines

## Core Principle

Agents must implement ONLY what is explicitly specified in requirements, prompts, or user instructions. Do not make assumptions or add functionality that is not directly requested or confirmed by the user.

## Strict Implementation Rules

### 1. Literal Interpretation Only

**Rule**: Implement exactly what is specified, nothing more.

**Examples**:
- If a requirement mentions "UserID", implement only the UserID field/parameter
- Do NOT automatically add user authentication, authorization, or user management systems
- If a prompt asks for "job search", implement only job search functionality
- Do NOT automatically add job application tracking, resume management, or notification systems

### 2. No Implicit Feature Addition

**Rule**: Never add features that seem "logical" or "commonly needed" without explicit confirmation.

**Prohibited Assumptions**:
- "Since there's a UserID, they probably need user authentication"
- "Since we're searching jobs, they probably want to save favorites"
- "Since we're processing data, they probably need data validation"
- "Since this is a web service, they probably need rate limiting"
- "Since we're storing data, they probably need backup and recovery"

### 3. Ask Before Extending

**Rule**: When you identify potential related functionality, ASK the user instead of implementing it.

**Correct Approach**:
```
"I notice you mentioned UserID in the requirements. Should I also implement:
- User authentication system?
- User profile management?
- User session handling?

Or should I only implement the UserID as a simple identifier field?"
```

**Incorrect Approach**:
```
"I'll implement UserID along with a complete user management system including 
authentication, authorization, profile management, and session handling."
```

### 4. Minimal Viable Implementation

**Rule**: Always choose the simplest implementation that satisfies the explicit requirements.

**Implementation Priority**:
1. **First**: Implement exactly what's specified
2. **Second**: Ask user about related functionality they might want
3. **Never**: Automatically add "helpful" features without confirmation

### 5. Data Fields Are Just Data Fields

**Rule**: A data field mentioned in requirements is just a data field unless explicitly specified otherwise.

**Examples**:
- `email` field = just store/use email string, NOT email validation system
- `password` field = just handle password data, NOT complete authentication system  
- `timestamp` field = just store/use timestamp, NOT complete audit logging system
- `status` field = just track status value, NOT complete workflow management system

### 6. Infrastructure Assumptions Prohibited

**Rule**: Do not assume infrastructure, security, or operational requirements unless explicitly stated.

**Prohibited Infrastructure Assumptions**:
- Database type or structure beyond what's specified
- Security measures beyond what's explicitly required
- Logging, monitoring, or alerting systems
- Error handling beyond basic error responses
- Performance optimizations not specifically requested
- Scalability features not explicitly required

### 7. Framework and Technology Neutrality

**Rule**: Do not assume specific technologies, frameworks, or architectural patterns unless specified.

**Stay Neutral On**:
- Database choice (SQL vs NoSQL vs file storage)
- Authentication methods (JWT vs sessions vs API keys)
- Communication protocols (REST vs GraphQL vs WebSocket)
- Deployment platforms (cloud vs on-premise vs containerized)
- Programming languages and frameworks

### 8. User Confirmation Required For

**Always ask user confirmation before adding**:
- Security features (authentication, authorization, encryption)
- Data validation beyond basic type checking
- Error handling beyond simple error responses
- Performance optimizations or caching
- Logging, monitoring, or analytics
- Backup, recovery, or data persistence strategies
- Integration with external services or APIs
- User interface enhancements not specified
- Business logic not explicitly described

## Implementation Examples

### ✅ Correct: Minimal Implementation

**Requirement**: "The system shall accept a UserID parameter"

**Correct Implementation**:
```python
def process_request(user_id: str):
    # Use the user_id as provided
    return {"processed_for_user": user_id}
```

### ❌ Incorrect: Over-Engineering

**Requirement**: "The system shall accept a UserID parameter"

**Incorrect Implementation**:
```python
class UserManager:
    def authenticate_user(self, user_id, password):
        # Added authentication without being asked
        pass
    
    def authorize_user(self, user_id, resource):
        # Added authorization without being asked
        pass
    
    def get_user_profile(self, user_id):
        # Added profile management without being asked
        pass

def process_request(user_id: str):
    user_manager = UserManager()
    if not user_manager.authenticate_user(user_id, password):
        raise AuthenticationError()
    # Over-engineered solution not requested
```

### ✅ Correct: Asking for Clarification

**Requirement**: "The system shall store job application data"

**Correct Response**:
```
"I can implement job application data storage. Should I include:
- Just basic job application fields (job_id, user_id, application_date)?
- Or do you also want application status tracking?
- Should I add application document storage?
- Do you need application history or audit trails?

Please specify exactly what job application data fields and functionality you need."
```

## Quality Assurance Checklist

Before implementing any feature, ask yourself:

- [ ] Is this functionality explicitly mentioned in the requirements?
- [ ] Am I adding features that "seem logical" but weren't requested?
- [ ] Am I making assumptions about what the user "probably wants"?
- [ ] Could I implement this more simply while still meeting the requirements?
- [ ] Should I ask the user about related functionality instead of assuming they want it?

## When In Doubt

**Always choose the minimal implementation and ask the user for clarification rather than making assumptions.**

It's better to implement too little and add more based on user feedback than to implement too much and have to remove unnecessary complexity.