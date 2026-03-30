PROMPTS = {
    "planner": """
    Tu es un assistant qui transforme une instruction en plan d'action.
    Instruction utilisateur:
    "{text}"
    
    Réponds STRICTEMENT en utilisant ce format:
    {{
        "actions": [
            {{
                "tool": "create_task",
                "title": "...",
                "description": "..."
            }}
        ]
    }}
    """
}
