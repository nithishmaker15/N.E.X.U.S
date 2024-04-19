''' <Project N.E.X.U.S, An Interactive AI>
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


import speech_recognition as sr # The Speech Recognition Library - Online based.
import LLM                      # Custom Library to outsource prompts to GEMINI (GOOGLE) API
import win32com.client          # The Local TTS (Text-to-Speech) wrapper

import pyfiglet                 # Both PYFIGLET and RICH are for creative visualization in the commandline (CMD)
from rich import print as console

console(f'[red]Successfully imported all modules.... (NEXUS)[/red]')

title = pyfiglet.figlet_format('N.E.X.U.S', font='isometric2')

console(f'[red]{title}[/red]')
#### STYLIZED N.E.X.U.S banner..... ####


        
class Nexus_CORE:


        def __init__(self, audio_cue, tts_rate = 1, tts_voice = 0.5, probe_time = 4 ):
                
                ####SETTING UP SOME CONSTANTS.....####
                
                self.audio_cue = audio_cue.lower()
                self.tts_rate = tts_rate
                self.tts_voice = tts_voice
                self.probe_time = probe_time
                
                ####SETTING UP SOME CONSTANTS.....####

                ####Initializing Recognizer module for speech recognition.....####
                
                self.recognizer = sr.Recognizer()

                ####SETTING UP TTS SETTINGS.....####
                
                self.speaker = win32com.client.Dispatch("SAPI.SpVoice") 
                self.speaker.Rate = self.tts_rate
                self.speaker.Voice = self.speaker.GetVoices().Item(self.tts_voice)

                ####SETTING UP TTS SETTINGS.....####

                

        def initiateNEXUS(self):
              
                
                
                
                with sr.Microphone() as self.microphone:
                        
                        while True:
                                #### Listen for 1 second to calibrate the energy threshold for ambient noise levels..... ####
                                self.recognizer.adjust_for_ambient_noise(self.microphone)
                                console(f'[red]Searching for Audio cue... (NEXUS)[/red]')
                                
                                self.command = self.recognizer.listen(self.microphone, phrase_time_limit=self.probe_time)
                                #### Outputs audio_data to pass through the Recognizer..... ####
                          
                                
                                try:
                                        self.command = self.recognizer.recognize_google(self.command)
                                        #### Recognize speech using Google Speech Recognition..... ####
                                        
                                        
                                        print('Extracted: '+self.command) #Extracted Text is displayed.....
                                        print('')
                            
                                        self.wakeword = self.command.split()[0].lower()
                                        #### Searches for a wakeword, simillar to 'Hey, SIRI!'..... ####
                                        
                                        
                                        if self.wakeword == self.audio_cue:
                                                
                                                self.response = LLM.GEMINI_LLM().run_CLOUD(self.command)
                                                #### Runs the command through the GEMINI API, and returns a response..... ####
                                        
                                                print('N.E.X.U.S: ' + self.response)
                                                print('')
                                                
                                                self.speaker.Speak(self.response)
                                                #### Converts response to spoken audio using TTS API..... ####
                                                
                                        else:
                                                pass
                                        #### Continues to search for a wakeword if none found..... ####

                                except Exception as error:
                                        pass
                                
                                       
                        
      
Nexus_CORE('Nexus').initiateNEXUS()
