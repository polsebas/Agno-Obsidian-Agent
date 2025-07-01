import requests
from abc import ABC, abstractmethod

class ObsidianMCPClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint.rstrip("/")

    def list_notes(self) -> list[str]:
        resp = requests.get(f"{self.endpoint}/list_notes")
        resp.raise_for_status()
        return resp.json()

    def read_note(self, note_id: str) -> str:
        resp = requests.get(f"{self.endpoint}/read_note/{note_id}")
        resp.raise_for_status()
        return resp.text

    def write_note(self, note_id: str, content: str) -> None:
        resp = requests.post(
            f"{self.endpoint}/write_note/{note_id}", json={"content": content}
        )
        resp.raise_for_status()