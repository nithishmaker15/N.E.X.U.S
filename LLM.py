''' <LLM for N.E.X.U.S>
    Copyright (C) 2024 Nithish M

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.'''



import google.generativeai as genai
import json

api_key = open(r"C:\NEXUS\_references_/API_KEY.txt", "r").read()
pre_prompt = open(r"C:\NEXUS\_references_/PERSONALITY_CORE.txt", "r").read()




safe = [ {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    }
]


class GEMINI_LLM():
# Initiated FALCOM LLM ( hopefully open source )




  def __init__(self):
      genai.configure(api_key=api_key)
      self.model = genai.GenerativeModel('gemini-1.5-pro-latest',system_instruction=pre_prompt)
     
   
    
  
  def run_CLOUD(self, prompt):
      response = self.model.generate_content(prompt,safety_settings=safe)
      try:
          out = response.text
      except ValueError:
          print(response.prompt_feedback)
          print(response.candidates[0].finish_reason)
          print(response.candidates[0].safety_ratings)

          out = ''
      return out
      
      
      


