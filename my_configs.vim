colorscheme papercolor
set nu
map <C-i> :set wrap<CR>
map <C-o> :set nowrap sidescroll=1 siso=15<CR>

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

" => elm-vim
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:elm_syntastic_show_warnings = 1
let g:ycm_semantic_triggers = {'elm' : ['.']}
