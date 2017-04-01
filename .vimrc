syntax on
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'neovimhaskell/haskell-vim'
Plugin 'tpope/vim-pathogen'
Plugin 'vim-scripts/VimClojure'
Plugin 'tpope/vim-fireplace'
Plugin 'VundleVim/Vundle.vim'
Plugin 'jimenezrick/vimerl'
Plugin 'vimwiki/vimwiki'
Plugin 'wlangstroth/vim-racket'
Plugin 'derekwyatt/vim-scala'
Plugin 'fatih/vim-go'
Plugin 'elixir-lang/vim-elixir'
Plugin 'slashmili/alchemist.vim'
" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
Plugin 'L9'
" Git plugin not hosted on GitHub
"Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
"Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
"Plugin 'ascenator/L9', {'name': 'newL9'}
Plugin 'Glench/Vim-Jinja2-Syntax'
Plugin 'tomasr/molokai'
Plugin 'scrooloose/nerdtree'
Plugin 'Valloric/YouCompleteMe'
Plugin 'Valloric/ListToggle'
Plugin 'scrooloose/syntastic'
"Plugin 'artur-shaik/vim-javacomplete2'
" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
:set nu
:colorscheme molokai
let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
:set t_Co=256
let g:EclimCompletionMethod = 'omnifunc'
hi Normal ctermfg=252 ctermbg=none
"For Haskell
let g:haskell_enable_quantification = 1   " to enable highlighting of `forall`
let g:haskell_enable_recursivedo = 1      " to enable highlighting of `mdo` and `rec`
let g:haskell_enable_arrowsyntax = 1      " to enable highlighting of `proc`
let g:haskell_enable_pattern_synonyms = 1 " to enable highlighting of `pattern`
let g:haskell_enable_typeroles = 1        " to enable highlighting of type roles
let g:haskell_enable_static_pointers = 1  " to enable highlighting of `static`
"For java
"autocmd FileType java setlocal omnifunc=javacomplete#Complete
"nmap <F4> <Plug>(JavaComplete-Imports-AddSmart)
"imap <F4> <Plug>(JavaComplete-Imports-AddSmart)
"nmap <leader>jI <Plug>(JavaComplete-Imports-AddMissing)
"nmap <leader>jR <Plug>(JavaComplete-Imports-RemoveUnused)
"nmap <leader>ji <Plug>(JavaComplete-Imports-AddSmart)
"nmap <leader>jii <Plug>(JavaComplete-Imports-Add)
"imap <C-j>I <Plug>(JavaComplete-Imports-AddMissing)
"imap <C-j>R <Plug>(JavaComplete-Imports-RemoveUnused)
"imap <C-j>i <Plug>(JavaComplete-Imports-AddSmart)
"imap <C-j>ii <Plug>(JavaComplete-Imports-Add)
"nmap <leader>jM <Plug>(JavaComplete-Generate-AbstractMethods)
"imap <C-j>jM <Plug>(JavaComplete-Generate-AbstractMethods)
"nmap <leader>jA <Plug>(JavaComplete-Generate-Accessors)
"nmap <leader>js <Plug>(JavaComplete-Generate-AccessorSetter)
"nmap <leader>jg <Plug>(JavaComplete-Generate-AccessorGetter)
"nmap <leader>ja <Plug>(JavaComplete-Generate-AccessorSetterGetter)
"nmap <leader>jts <Plug>(JavaComplete-Generate-ToString)
"nmap <leader>jeq <Plug>(JavaComplete-Generate-EqualsAndHashCode)
"nmap <leader>jc <Plug>(JavaComplete-Generate-Constructor)
"nmap <leader>jcc <Plug>(JavaComplete-Generate-DefaultConstructor)
"imap <C-j>s <Plug>(JavaComplete-Generate-AccessorSetter)
"imap <C-j>g <Plug>(JavaComplete-Generate-AccessorGetter)
"imap <C-j>a <Plug>(JavaComplete-Generate-AccessorSetterGetter)
"vmap <leader>js <Plug>(JavaComplete-Generate-AccessorSetter)
"vmap <leader>jg <Plug>(JavaComplete-Generate-AccessorGetter)
"vmap <leader>ja <Plug>(JavaComplete-Generate-AccessorSetterGetter)
let g:syntastic_enable_racket_racket_checker = 1
