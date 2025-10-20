# Memory Interface Specification Template

## Basic Memory Operations

### Core Interface
```
interface SimpleMemoryManager {
  createEntry(content: Object, category: string, ttlSeconds: number): MemoryReference
  validateReference(reference: MemoryReference): boolean
  cleanupExpired(references: MemoryReference[]): number
}
```

### Memory Reference Structure
```
class MemoryReference {
  id: string
  category: string
  expiresAt: Date
  
  isExpired(): boolean
  serialize(): string
}
```

### Memory Categories
- **working**: Short-term session data (1 hour default)
- **episodic**: Conversation history (1 day default)  
- **semantic**: Facts and knowledge (1 week default)

### Usage Example
```javascript
// Create memory entry
const ref = memoryManager.createEntry(
  {userPreference: "dark mode"}, 
  "working", 
  3600
);

// Share reference between agents
const referenceId = ref.id;

// Validate before use
if (memoryManager.validateReference(ref)) {
  // Use the reference
}
```

## Implementation Notes
- Keep references lightweight for agent communication
- Implement simple expiration checking
- Use basic cleanup for expired references
- No complex features unless explicitly needed