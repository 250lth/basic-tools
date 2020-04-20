let g:seiya_auto_enable=1
colorscheme PaperColor
set nu
map <C-i> :set wrap<CR>
map <C-o> :set nowrap sidescroll=1 siso=15<CR>
set splitbelow
set cursorline

" tab styles
autocmd filetype javascript setlocal shiftwidth=2 tabstop=2
autocmd filetype html setlocal shiftwidth=2 tabstop=2
autocmd filetype css setlocal shiftwidth=2 tabstop=2
autocmd filetype vue setlocal shiftwidth=2 tabstop=2
autocmd filetype elm setlocal shiftwidth=2 tabstop=2
autocmd filetype idris setlocal shiftwidth=2 tabstop=2
autocmd filetype yaml setlocal shiftwidth=2 tabstop=2
autocmd filetype haskell setlocal shiftwidth=2 tabstop=2
autocmd filetype dart setlocal shiftwidth=2 tabstop=2
autocmd filetype scala setlocal shiftwidth=2 tabstop=2
autocmd filetype sbt setlocal shiftwidth=2 tabstop=2

" => vim-vue
autocmd FileType vue syntax sync fromstart

" => haskell-vim
let g:haskell_enable_quantification = 1   " to enable highlighting of `forall`
let g:haskell_enable_recursivedo = 1      " to enable highlighting of `mdo` and `rec`
let g:haskell_enable_arrowsyntax = 1      " to enable highlighting of `proc`
let g:haskell_enable_pattern_synonyms = 1 " to enable highlighting of `pattern`
let g:haskell_enable_typeroles = 1        " to enable highlighting of type roles
let g:haskell_enable_static_pointers = 1  " to enable highlighting of `static`
let g:haskell_backpack = 1                " to enable highlighting of backpack keywords

" => neco-ghc
let g:haskellmode_completion_ghc = 0
autocmd FileType haskell setlocal omnifunc=necoghc#omnifunc
let g:ycm_semantic_triggers = {'haskell' : ['.']}

" => nerd tree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
let g:NERDTreeShowHidden=1

" => elm-vim
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:elm_syntastic_show_warnings = 1
let g:ycm_semantic_triggers = {'elm' : ['.']}

" => vim-javascript
let g:javascript_plugin_jsdoc = 1
let g:javascript_plugin_ngdoc = 1
let g:javascript_plugin_flow = 1
augroup javascript_folding
    au!
    au FileType javascript setlocal foldmethod=syntax
augroup END

" => emment-vim
let g:user_emmet_install_global = 0
autocmd FileType html,css EmmetInstall

" => idris-vim
let g:idris_indent_if = 3
let g:idris_indent_case = 5
let g:idris_indent_let = 4
let g:idris_indent_where = 6
let g:idris_indent_do = 3
let g:idris_indent_rewrite = 8
let g:idris_conceal = 1

" => vim-javacomplete2
autocmd FileType java setlocal omnifunc=javacomplete#Complete
let g:JavaComplete_EnableDefaultMappings = 0

" => dart-vim-plugin
let dart_html_in_string=v:true
let dart_style_guide = 2
let dart_format_on_save = 1
