doc = '''
#%RAML 1.0
title: Event Manager
version: 1.0.0
securitySchemes:
    JWT:
        description: |
            Event Manager supports JWT for authenticating all API requests.
        pattern: '[a-zA-Z0-9\-_]+?\.[a-zA-Z0-9\-_]+?\.([a-zA-Z0-9\-_]+)?'
        properties:
        alg:
            enum: [HS256, HS512]
        type:
            enum: [Auth]
        describedBy: 
            headers: 
                Authorization:
                    description: X-AuthToken
                    type: string
                    required: true
            responses: 
                401: "Acesso Negado"
        settings:
            roles: []
types:
    Auth:
        type: object
        discriminator: token
        properties:
          token : string
    Event:
        type: object
        discriminator: event
        description: |
            Model for the Event Table
        properties:
            event_id: 
                type: integer
            agent_id:
                type: integer
            level:
                type: string
            payload:
                type: string
            shelved:
                type: boolean
            date:
                type: datetime
        example: 
            event_id: 
                value: 1
            agent_id: 
                value: 2
            level: 
                value: 'critical'
            payload: 
                value: '000111AAAbbb'
            data: 
                value: '2020-02-02T10:00:00:00Z'
            shelve: 
                value: False
        
    Agent:
        type: object
        discriminator: ag
        description: |
            Model for the Agent Table
        properties:
            agent_id: 
                type: integer
            user_id: 
                type: integer
            name: 
                type: string
            status:
                type: boolean
            environment:
                type: string
            version:
                type: string
            address:
                type: string
        example:
            {
                agent_id: 1,
                user_id: 2,
                name: "linux-server",
                status: True,
                environment: "production",
                version: '1.1.1',
                address: '10.0.34.15',
            }
    Group:
        type: object
        discriminator: grp
        description: |
            Model for the Group Table
        properties:
            group_id:
                type: integer
            name:
                type: string
        example:
            {
                group_id: 1,
                name: 'admin',
            }
    User:
        type: object
        discriminator: usr
        description: |
            Model for the User Table
        properties:
            name: 
                type: string
            user_id:
                type: integer
            email:
                type: string
            last_login:
                type: datetime
            group_id:
                type: integer

/auth/token:
    post:
        description: |
            Request for recovering the access token
        body:
            application/json:
                username:
                    type: string
                password:
                    type: string
        tags: 
        - "Token"
        summary: "Validates Token"
        responses:
            201:
                body: "Success"
            400:
                body: "Denyed"
/agents:
    post:
        description: |
            Creates a new agent
        securedBy: [JWT]
        body:
            application/json:
                properties:
                    headers:
                        Content-Type: 'application/json'
                        body:
                            type: Agent
                example:
                    {
                        agent_id: 1,
                        user_id: 2,
                        name: "linux-server",
                        status: True,
                        environment: "production",
                        version: '1.1.1',
                        address: '10.0.34.15',
                    }
        responses:
            201:
                body: "Created"
            401:
                body: "Unauthorized"
        tags:
        - "Agent"
        summary: "Create a new Agent"
    get:
        description: |
            List all agents
        securedBy: [JWT]
        tags:
        - "Agent"
        summary: "List all the agents"
        responses:
            200:
                body: Agent[]
    /{id}:
        get:
            description: |
                List a specific agent
            securedBy: [JWT]
            tags:
            - "Agent"
            summary: "List a specific agent"
            responses: 
                200:
                    body: Agent[]
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
        put:
            description: |
                Modify a specific agent
            securedBy: [JWT]
            responses: 
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
        delete:
            description: |
                Modify a specific agent
            securedBy: [JWT]
            responses: 
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
            
    /{id}/events:
        post:
            description: |
                Create a event related to a agent
            securedBy: [JWT]
            body:
                application/json:
                    type: Event
                201:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
            
        get:
            description: |
                List all events related to a agent
            securedBy: [JWT]
            tags:
            - "Event"
            summary: "List all events from a agent"
            responses: 
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
        put:
            description: |
                Modify an event related to a agent
            securedBy: [JWT]
            tags:
            - "Event"
            summary: "List all events from a agent"
            body:
                application/json: 
                    type: Event[]
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
        delete:
            description: |
                Delete an event related to a agent
            securedBy: [JWT]
            tags:
            - "Event"
            body:
                application/json: 
                    type: Event[]
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"

/users:
    post:
        description: |
            Create a new user
        securedBy: [JWT]
        tags:
        - "User"
        summary: "Create a new User"
        body:
            application/json:
                properties:
                    body: User[]
        responses:
            201:
                body: "Success"
            401:
                body: "Unauthorized"
    get:
        description: |
            List all users
        securedBy: [JWT]
        tags:
        - "User"
        summary: "List all Users"
        responses:
            200:
                body: User[]
    /{id}:
        get:
            description: |
                List a specific User
            securedBy: [JWT]
            tags:
            - "User"
            summary: "List a specific User"
            responses:
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
        put:
            description: |
                "Modify a specific User"
            securedBy: [JWT]
            tags:
            - "User"
            summary: "Modify a specific User"
            responses:
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
        delete:
            description: |
                "Delete a specific User"
            securedBy: [JWT]
            tags:
            - "User"
            summary: "Modify a specific User"
            responses:
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"

/groups:
    post:
        description: |
            "Create a Group"
        securedBy: [JWT]
        tags:
        - "Group"
        summary: "Create a new group"
        body:
            application/json:
                properties:
                    type: Group
                example: 
                    {
                        group_id: 1,
                        name: 'admin',
                    }
        responses:
            201:
                body: "Success"
            401:
                body: "Unauthorized"
    get:
        description: |
            "List all Groups"
        securedBy: [JWT]
        tags:
        - "Group"
        summary: "Create a new group"
        responses:
            200:
                body: "Success"
            401:
                body: "Unauthorized"

    /{id}:
        get:
            description: |
                "List a specific Group"
            securedBy: [JWT]
            tags:
            - "Group"
            summary: "Create a new group"
            responses:
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
        
        put:
            description: |
                "modify a specific Group"
            securedBy: [JWT]
            tags:
            - "Group"
            summary: "Create a new group"
            responses:
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
        
        delete:
            description: |
                "delete a specific Group"
            securedBy: [JWT]
            tags:
            - "Group"
            summary: "Create a new group"
            responses:
                200:
                    body: "Success"
                401:
                    body: "Unauthorized"
                404:
                    body: "Not Found"
        
'''