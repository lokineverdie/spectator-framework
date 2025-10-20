# Memory Management Framework Integration Guide

## Overview

This guide provides integration patterns for implementing the Memory Management System across different frameworks and platforms. The system maintains technology neutrality while providing concrete implementation guidance for popular frameworks.

## Integration Principles

### Technology-Neutral Design
- Memory interfaces remain consistent across all platforms
- Storage adapters provide platform-specific implementations
- Reference patterns work identically regardless of underlying technology

### Framework-Agnostic Patterns
- Standard memory reference format across all implementations
- Consistent API contracts for all storage backends
- Uniform error handling and validation patterns

## Major Framework Integration Patterns

### Node.js/JavaScript Frameworks

#### Express.js Integration
```javascript
// Memory service integration with Express.js
const express = require('express');
const { MemoryManager, FileStorageAdapter } = require('./memory-system');

const app = express();
const memoryManager = new MemoryManager({
  storage: new FileStorageAdapter('./memory-data')
});

// Middleware for memory reference handling
app.use('/api', (req, res, next) => {
  req.memoryManager = memoryManager;
  next();
});

// Agent endpoint with memory reference response
app.post('/api/agent/search', async (req, res) => {
  const searchResults = await performSearch(req.body.query);
  
  // Store results and return reference
  const memoryRef = await req.memoryManager.store({
    category: 'working_memory',
    content: searchResults,
    metadata: { operation: 'search', query: req.body.query }
  });
  
  res.json({
    status: 'success',
    summary: `Found ${searchResults.length} results`,
    memoryReference: memoryRef.serialize()
  });
});
```

#### Next.js Integration
```javascript
// pages/api/memory/[operation].js
import { MemoryManager, DatabaseStorageAdapter } from '../../../lib/memory-system';

const memoryManager = new MemoryManager({
  storage: new DatabaseStorageAdapter(process.env.DATABASE_URL)
});

export default async function handler(req, res) {
  const { operation } = req.query;
  
  switch (operation) {
    case 'store':
      const reference = await memoryManager.store(req.body);
      res.json({ reference: reference.serialize() });
      break;
      
    case 'retrieve':
      const data = await memoryManager.retrieve(req.body.reference);
      res.json({ data });
      break;
      
    default:
      res.status(400).json({ error: 'Invalid operation' });
  }
}
```

### Python Frameworks

#### FastAPI Integration
```python
from fastapi import FastAPI, HTTPException
from memory_system import MemoryManager, SQLiteStorageAdapter
from pydantic import BaseModel

app = FastAPI()
memory_manager = MemoryManager(storage=SQLiteStorageAdapter("memory.db"))

class MemoryRequest(BaseModel):
    category: str
    content: dict
    metadata: dict = {}

class AgentResponse(BaseModel):
    status: str
    summary: str
    memory_reference: str

@app.post("/agent/analyze", response_model=AgentResponse)
async def analyze_data(request: MemoryRequest):
    # Perform analysis
    analysis_results = await perform_analysis(request.content)
    
    # Store results and return reference
    memory_ref = await memory_manager.store({
        "category": "working_memory",
        "content": analysis_results,
        "metadata": {"operation": "analysis", **request.metadata}
    })
    
    return AgentResponse(
        status="success",
        summary=f"Analysis complete with {len(analysis_results)} insights",
        memory_reference=memory_ref.serialize()
    )
```

#### Django Integration
```python
# views.py
from django.http import JsonResponse
from django.views import View
from memory_system import MemoryManager, PostgreSQLStorageAdapter
import json

class MemoryView(View):
    def __init__(self):
        super().__init__()
        self.memory_manager = MemoryManager(
            storage=PostgreSQLStorageAdapter(
                host=settings.DB_HOST,
                database=settings.DB_NAME
            )
        )
    
    def post(self, request):
        data = json.loads(request.body)
        
        if request.path.endswith('/store'):
            reference = self.memory_manager.store(data)
            return JsonResponse({'reference': reference.serialize()})
            
        elif request.path.endswith('/retrieve'):
            memory_data = self.memory_manager.retrieve(data['reference'])
            return JsonResponse({'data': memory_data})
```

### Java/Spring Framework

#### Spring Boot Integration
```java
@RestController
@RequestMapping("/api/memory")
public class MemoryController {
    
    private final MemoryManager memoryManager;
    
    public MemoryController() {
        this.memoryManager = new MemoryManager(
            new JpaStorageAdapter(entityManager)
        );
    }
    
    @PostMapping("/agent/process")
    public ResponseEntity<AgentResponse> processData(@RequestBody ProcessRequest request) {
        // Process data
        ProcessResult result = dataProcessor.process(request.getData());
        
        // Store result and return reference
        MemoryReference reference = memoryManager.store(MemoryEntry.builder()
            .category(MemoryCategory.WORKING_MEMORY)
            .content(result)
            .metadata(Map.of("operation", "process"))
            .build());
        
        return ResponseEntity.ok(AgentResponse.builder()
            .status("success")
            .summary("Processing complete")
            .memoryReference(reference.serialize())
            .build());
    }
}
```

### .NET/ASP.NET Core Integration

#### ASP.NET Core Integration
```csharp
[ApiController]
[Route("api/[controller]")]
public class MemoryController : ControllerBase
{
    private readonly IMemoryManager _memoryManager;
    
    public MemoryController(IMemoryManager memoryManager)
    {
        _memoryManager = memoryManager;
    }
    
    [HttpPost("agent/transform")]
    public async Task<IActionResult> TransformData([FromBody] TransformRequest request)
    {
        // Transform data
        var transformResult = await _dataTransformer.Transform(request.Data);
        
        // Store result and return reference
        var memoryRef = await _memoryManager.StoreAsync(new MemoryEntry
        {
            Category = MemoryCategory.WorkingMemory,
            Content = transformResult,
            Metadata = new Dictionary<string, object> { ["operation"] = "transform" }
        });
        
        return Ok(new AgentResponse
        {
            Status = "success",
            Summary = "Transformation complete",
            MemoryReference = memoryRef.Serialize()
        });
    }
}
```

## Memory Reference Patterns by Platform

### JavaScript/TypeScript Pattern
```typescript
interface MemoryReference {
  id: string;
  category: 'working_memory' | 'episodic_memory' | 'semantic_memory' | 'procedural_memory';
  contentType: string;
  estimatedSize: number;
  expiresAt: Date;
  metadata?: Record<string, any>;
}

class MemoryReferenceImpl implements MemoryReference {
  constructor(
    public id: string,
    public category: MemoryCategory,
    public contentType: string,
    public estimatedSize: number,
    public expiresAt: Date,
    public metadata: Record<string, any> = {}
  ) {}
  
  serialize(): string {
    return JSON.stringify({
      id: this.id,
      category: this.category,
      contentType: this.contentType,
      estimatedSize: this.estimatedSize,
      expiresAt: this.expiresAt.toISOString(),
      metadata: this.metadata
    });
  }
  
  static deserialize(data: string): MemoryReference {
    const parsed = JSON.parse(data);
    return new MemoryReferenceImpl(
      parsed.id,
      parsed.category,
      parsed.contentType,
      parsed.estimatedSize,
      new Date(parsed.expiresAt),
      parsed.metadata
    );
  }
}
```

### Python Pattern
```python
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, Any, Optional
import json

@dataclass
class MemoryReference:
    id: str
    category: str
    content_type: str
    estimated_size: int
    expires_at: datetime
    metadata: Optional[Dict[str, Any]] = None
    
    def serialize(self) -> str:
        data = asdict(self)
        data['expires_at'] = self.expires_at.isoformat()
        return json.dumps(data)
    
    @classmethod
    def deserialize(cls, data: str) -> 'MemoryReference':
        parsed = json.loads(data)
        parsed['expires_at'] = datetime.fromisoformat(parsed['expires_at'])
        return cls(**parsed)
    
    def is_expired(self) -> bool:
        return datetime.now() > self.expires_at
```

### Java Pattern
```java
public class MemoryReference {
    private final String id;
    private final MemoryCategory category;
    private final String contentType;
    private final int estimatedSize;
    private final Instant expiresAt;
    private final Map<String, Object> metadata;
    
    // Constructor, getters, etc.
    
    public String serialize() {
        return JsonUtils.toJson(Map.of(
            "id", id,
            "category", category.name(),
            "contentType", contentType,
            "estimatedSize", estimatedSize,
            "expiresAt", expiresAt.toString(),
            "metadata", metadata
        ));
    }
    
    public static MemoryReference deserialize(String data) {
        Map<String, Object> parsed = JsonUtils.fromJson(data, Map.class);
        return new MemoryReference(
            (String) parsed.get("id"),
            MemoryCategory.valueOf((String) parsed.get("category")),
            (String) parsed.get("contentType"),
            (Integer) parsed.get("estimatedSize"),
            Instant.parse((String) parsed.get("expiresAt")),
            (Map<String, Object>) parsed.get("metadata")
        );
    }
}
```

### C# Pattern
```csharp
public class MemoryReference
{
    public string Id { get; set; }
    public MemoryCategory Category { get; set; }
    public string ContentType { get; set; }
    public int EstimatedSize { get; set; }
    public DateTime ExpiresAt { get; set; }
    public Dictionary<string, object> Metadata { get; set; } = new();
    
    public string Serialize()
    {
        return JsonSerializer.Serialize(new
        {
            Id,
            Category = Category.ToString(),
            ContentType,
            EstimatedSize,
            ExpiresAt,
            Metadata
        });
    }
    
    public static MemoryReference Deserialize(string data)
    {
        var parsed = JsonSerializer.Deserialize<Dictionary<string, object>>(data);
        return new MemoryReference
        {
            Id = parsed["Id"].ToString(),
            Category = Enum.Parse<MemoryCategory>(parsed["Category"].ToString()),
            ContentType = parsed["ContentType"].ToString(),
            EstimatedSize = Convert.ToInt32(parsed["EstimatedSize"]),
            ExpiresAt = DateTime.Parse(parsed["ExpiresAt"].ToString()),
            Metadata = (Dictionary<string, object>)parsed["Metadata"]
        };
    }
}
```

## Storage Implementation Examples

### File-Based Storage
```javascript
// Simple file-based storage adapter
class FileStorageAdapter {
  constructor(basePath) {
    this.basePath = basePath;
    this.ensureDirectory();
  }
  
  async store(entry) {
    const reference = this.createReference(entry);
    const filePath = path.join(this.basePath, `${reference.id}.json`);
    
    await fs.writeFile(filePath, JSON.stringify({
      reference: reference.serialize(),
      content: entry.content,
      metadata: entry.metadata,
      createdAt: new Date().toISOString()
    }));
    
    return reference;
  }
  
  async retrieve(reference) {
    const filePath = path.join(this.basePath, `${reference.id}.json`);
    
    if (!await fs.exists(filePath)) {
      return null;
    }
    
    const data = JSON.parse(await fs.readFile(filePath, 'utf8'));
    return {
      content: data.content,
      metadata: data.metadata,
      createdAt: new Date(data.createdAt)
    };
  }
}
```

### Database Storage (SQL)
```python
class SQLStorageAdapter:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.setup_tables()
    
    def setup_tables(self):
        metadata = MetaData()
        self.memory_table = Table('memory_entries', metadata,
            Column('id', String, primary_key=True),
            Column('category', String, nullable=False),
            Column('content_type', String, nullable=False),
            Column('content', JSON, nullable=False),
            Column('metadata', JSON),
            Column('created_at', DateTime, default=datetime.utcnow),
            Column('expires_at', DateTime),
            Column('estimated_size', Integer)
        )
        metadata.create_all(self.engine)
    
    async def store(self, entry):
        reference = self.create_reference(entry)
        
        with self.engine.connect() as conn:
            conn.execute(self.memory_table.insert().values(
                id=reference.id,
                category=reference.category,
                content_type=reference.content_type,
                content=entry.content,
                metadata=entry.metadata,
                expires_at=reference.expires_at,
                estimated_size=reference.estimated_size
            ))
            conn.commit()
        
        return reference
    
    async def retrieve(self, reference):
        with self.engine.connect() as conn:
            result = conn.execute(
                self.memory_table.select().where(
                    self.memory_table.c.id == reference.id
                )
            ).fetchone()
            
            if not result:
                return None
                
            return MemoryEntry(
                content=result.content,
                metadata=result.metadata,
                created_at=result.created_at
            )
```

### NoSQL Storage (MongoDB)
```javascript
class MongoStorageAdapter {
  constructor(connectionString, databaseName) {
    this.client = new MongoClient(connectionString);
    this.db = this.client.db(databaseName);
    this.collection = this.db.collection('memory_entries');
  }
  
  async store(entry) {
    const reference = this.createReference(entry);
    
    await this.collection.insertOne({
      _id: reference.id,
      category: reference.category,
      contentType: reference.contentType,
      content: entry.content,
      metadata: entry.metadata,
      createdAt: new Date(),
      expiresAt: reference.expiresAt,
      estimatedSize: reference.estimatedSize
    });
    
    return reference;
  }
  
  async retrieve(reference) {
    const document = await this.collection.findOne({
      _id: reference.id
    });
    
    if (!document) {
      return null;
    }
    
    return {
      content: document.content,
      metadata: document.metadata,
      createdAt: document.createdAt
    };
  }
  
  async cleanup(expiredBefore) {
    const result = await this.collection.deleteMany({
      expiresAt: { $lt: expiredBefore }
    });
    
    return { deletedCount: result.deletedCount };
  }
}
```

### Cloud Storage (AWS S3)
```python
import boto3
import json
from datetime import datetime

class S3StorageAdapter:
    def __init__(self, bucket_name, region='us-east-1'):
        self.s3_client = boto3.client('s3', region_name=region)
        self.bucket_name = bucket_name
        
    async def store(self, entry):
        reference = self.create_reference(entry)
        
        # Store content in S3
        content_key = f"memory/{reference.id}/content.json"
        metadata_key = f"memory/{reference.id}/metadata.json"
        
        # Upload content
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=content_key,
            Body=json.dumps(entry.content),
            ContentType='application/json',
            Metadata={
                'memory-id': reference.id,
                'category': reference.category,
                'expires-at': reference.expires_at.isoformat()
            }
        )
        
        # Upload metadata
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=metadata_key,
            Body=json.dumps({
                'reference': reference.serialize(),
                'metadata': entry.metadata,
                'created_at': datetime.utcnow().isoformat()
            }),
            ContentType='application/json'
        )
        
        return reference
    
    async def retrieve(self, reference):
        try:
            content_key = f"memory/{reference.id}/content.json"
            metadata_key = f"memory/{reference.id}/metadata.json"
            
            # Get content
            content_response = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=content_key
            )
            content = json.loads(content_response['Body'].read())
            
            # Get metadata
            metadata_response = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=metadata_key
            )
            metadata_info = json.loads(metadata_response['Body'].read())
            
            return MemoryEntry(
                content=content,
                metadata=metadata_info['metadata'],
                created_at=datetime.fromisoformat(metadata_info['created_at'])
            )
            
        except self.s3_client.exceptions.NoSuchKey:
            return None
```

## Integration Best Practices

### Error Handling Patterns
```javascript
// Consistent error handling across platforms
class MemoryError extends Error {
  constructor(message, code, details = {}) {
    super(message);
    this.code = code;
    this.details = details;
  }
}

// Usage in storage adapter
async store(entry) {
  try {
    // Storage implementation
    return reference;
  } catch (error) {
    throw new MemoryError(
      'Failed to store memory entry',
      'STORAGE_ERROR',
      { originalError: error.message, entryId: entry.id }
    );
  }
}
```

### Configuration Management
```yaml
# memory-config.yml - Framework-agnostic configuration
memory_system:
  storage:
    type: "postgresql"  # file, mongodb, s3, etc.
    connection:
      host: "${DB_HOST}"
      database: "${DB_NAME}"
      
  categories:
    working_memory:
      retention_days: 1
      compression_enabled: false
      
    episodic_memory:
      retention_days: 30
      compression_enabled: true
      
  performance:
    cache_size: 1000
    cleanup_interval: 3600
```

### Testing Integration
```javascript
// Framework-agnostic testing patterns
describe('Memory System Integration', () => {
  let memoryManager;
  
  beforeEach(() => {
    // Use in-memory adapter for testing
    memoryManager = new MemoryManager({
      storage: new InMemoryStorageAdapter()
    });
  });
  
  test('should store and retrieve memory entries', async () => {
    const entry = {
      category: 'working_memory',
      content: { test: 'data' },
      metadata: { source: 'test' }
    };
    
    const reference = await memoryManager.store(entry);
    const retrieved = await memoryManager.retrieve(reference);
    
    expect(retrieved.content).toEqual(entry.content);
  });
});
```

## Platform-Specific Considerations

### Node.js/JavaScript
- Use async/await for all memory operations
- Implement proper error handling with try/catch
- Consider memory usage for large datasets
- Use streams for large content processing

### Python
- Use asyncio for asynchronous operations
- Implement proper type hints for better IDE support
- Consider using dataclasses for memory models
- Use context managers for resource cleanup

### Java/Spring
- Use CompletableFuture for asynchronous operations
- Implement proper exception handling
- Use dependency injection for storage adapters
- Consider JPA entities for database storage

### .NET/C#
- Use async/await with ConfigureAwait(false)
- Implement proper disposal patterns
- Use dependency injection container
- Consider Entity Framework for database operations

This integration guide provides the foundation for implementing memory management across any technology stack while maintaining consistency and framework principles.