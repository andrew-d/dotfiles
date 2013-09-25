" Vim syntax file
" Language:	Underscore.js Templates
" Maintainer:	Martin Schuerrer, @MSch <martin@schuerrer.org>
" Modified By:  Andrew Dunham, @andrew_dunham <andrew@du.nham.ca>
" Version:	3
" Last Change:  2013 Sept 25
"
" depending on your file extension, you can add this to your vimrc:
" au BufNewFile,BufRead *.jst set syntax=jst

" Read the HTML syntax to start with
runtime! syntax/html.vim
unlet b:current_syntax

if exists("b:current_syntax")
  finish
endif

" Note: order matters - the last defined groups are matched first, so we need
" to put the more general matches at the beginning.
syn region jstBlock matchgroup=jstDelim containedin=ALL start="<%" keepend end="%>" contains=@htmlJavaScript,htmlCssStyleComment,htmlScriptTag,@htmlPreproc
syn region jstBlock matchgroup=jstDelim containedin=ALL start="<%=" keepend end="%>" contains=@htmlJavaScript,htmlCssStyleComment,htmlScriptTag,@htmlPreproc
syn region jstBlock matchgroup=jstDelim containedin=ALL start="<%-" keepend end="%>" contains=@htmlJavaScript,htmlCssStyleComment,htmlScriptTag,@htmlPreproc

hi def link jstDelim PreProc

let b:current_syntax = "underscore_template"
