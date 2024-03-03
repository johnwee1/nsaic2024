# nsaic2024

## Pipeline:

Here's a manual pipeline of how to use the scripts in this folder. Not sure if we are going to automate this whole thing because there are a few checks to make.

1. To extract text from PDF files in the `textbook` directory:
Run `extract("filename.txt")` from `pdf_text_extractor.py`. The output is saved under the directory `raws`.

2. Split chunks from the long text file. **ANY CHANGES MADE TO PROMPT.TXT SHOULD BE MADE PRIOR TO THIS STEP.**
Run `text_splitter("filename")` (note: no .txt suffix here) which will split the texts while factoring in the context length of `prompt.txt`.

> I recommend manually inspecting the output of the split text before going to the next step

3. To prompt remote models, use the file `askgpt.py`. To use, change `FILE_PREFIX` on the very top to the name of the file without its `.txt` extension and run the script. Cross your fingers that it works. The output log will show a lot of info but if you see any filepaths at the end of the output it means that those texts have somehow failed to generate. I've implemented retry logic but not sure if it works all the time.

- The output of the file is in `"{FILE_PREFIX}_qns.txt"`, like "stanford_ml_notes_qns.txt".

> If this fails, you can manually copy the text output from the terminal and paste it into a txt file yourself.

4. _Experimental_: Sanitize outputs using `output_sanitizer.py`
I chatGPT'ed a txt file sanitizer that does certain checks and filters stuff. You can change this script if you want. **Remember to change the input and output filenames if you are running this script.**

> The cleaned questions as of now should be in separate files with different filenames, so that we don't accidentally end up overwriting the questions





