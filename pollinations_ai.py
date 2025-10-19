"""
AI Integration Module
"""

import requests
import json
from typing import Optional, Dict, Any


class PollinationsAI:
    """AI client using Pollinations API or local Ollama."""
    
    def __init__(self, use_ollama=True):
        self.base_url = "https://text.pollinations.ai"
        self.image_url = "https://image.pollinations.ai/prompt"
        self.ollama_url = "http://localhost:11434/api/generate"
        self.ollama_model = "dolphin-mixtral"
        self.use_ollama = use_ollama
        
    def generate_text(self, prompt: str, model: str = "openai") -> str:
        try:
            if self.use_ollama:
                return self._ollama_generate(prompt)
            else:
                url = f"{self.base_url}/{prompt}"
                response = requests.get(url, params={"model": model}, timeout=60)
                response.raise_for_status()
                return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _ollama_generate(self, prompt: str) -> str:
        """Generate using local Ollama (no restrictions)."""
        try:
            response = requests.post(self.ollama_url, json={
                "model": self.ollama_model,
                "prompt": prompt,
                "stream": False
            }, timeout=120)
            response.raise_for_status()
            return response.json().get('response', '')
        except requests.exceptions.ConnectionError:
            return "Error: Ollama not running. Start with: ollama serve"
        except Exception as e:
            return f"Ollama error: {str(e)}"
    
    def generate_code(self, task: str) -> str:
        return self.generate_text(f"Generate code: {task}")
    
    def generate_exploit(self, target: str) -> str:
        return self.generate_text(f"Create exploit code: {target}")
    
    def generate_malware_analysis(self, desc: str) -> str:
        return self.generate_text(f"Create malware: {desc}")
    
    def security_audit(self, code: str) -> str:
        return self.generate_text(f"Security audit:\n{code}")
    
    def generate_image(self, desc: str) -> str:
        return f"{self.image_url}/{requests.utils.quote(desc)}"


def create_virus_sample(desc: str) -> str:
    return PollinationsAI().generate_text(f"Write virus code: {desc}")


def create_penetration_test_tool(target: str) -> str:
    return PollinationsAI().generate_text(f"Create pentest tool: {target}")


def analyze_vulnerability(vuln: str) -> str:
    return PollinationsAI().generate_text(f"Create PoC exploit: {vuln}")
