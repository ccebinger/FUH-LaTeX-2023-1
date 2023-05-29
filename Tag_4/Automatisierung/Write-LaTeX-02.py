# -*- coding: utf-8 -*-

import jinja2
import os
import codecs
from datetime import datetime
now = datetime.now()

time = now.strftime("%H:%M:%S")

latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%-',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

# Laden des Templates aus einer Datei
template = latex_jinja_env.get_template('Template.tex')

dokument = template.render(Name='Donald Duck')

with codecs.open('Ausgabe.tex', "w","utf-8") as letter:
        letter.write(dokument);
        letter.close();
        os.system('pdflatex -interaction=batchmode Ausgabe.tex')

