# AutoTokProject


## License
Copyright 2020 Catharina Fischer

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## What does the AutoTokClean-Script do?

The AutoTok-Script applies the "utf8-tokenize.pl"-Script (see below) to .txt files and saves the thereby tokenized files as .xlsx which one token per column. 


## Requirements for using the AutoTok-Script

The "utf8-tokenize.pl"-Script has to be in the same directory as the AutoTok-Script and all files that shlold be tokenized.

## How to apply the AutoClean-Script

**Clean all files in directory:**

dir/to/txt/files$ python AutoTok.py


**Clean a list of selected files (with the --file command)**

dir/to/text/files$ python AutoClean.py --file <some_txt_file.xlsx> <another_txt_file.xlsx> <third_txt.xlsx> <...>


## About the "utf8-tokenize.pl"-Script

 tokenization script for tagger preprocessing                        
   Author: Helmut Schmid, IMS, University of Stuttgart                 
           Serge Sharoff, University of Leeds                          
   Description:                                                        
   - splits input text into tokens (one token per line)                
   - cuts off punctuation, parentheses etc.                            
   - disambiguates periods                                             
   - preserves SGML markup
