set nocompatible              " be iMproved
filetype off                  " required!
"set nu "active this command will let you see the line number
set fileencodings=utf-8,gbk   
set backspace=indent,eol,start 
set noswapfile                
"set lines=999 columns=999
set autoread                  
set modeline 

"new added by myself  - - - - - - - - - - - - - - - - - - - - 

"configure the cursor mode
":autocmd InsertEnter,InsertLeave * set cul!
if has("autocmd")
  au InsertEnter * silent execute "!gconftool-2 --type string --set /apps/gnome-terminal/profiles/Default/cursor_shape ibeam"    
  au InsertLeave * silent execute "!gconftool-2 --type string --set /apps/gnome-terminal/profiles/Default/cursor_shape block"
  au VimLeave * silent execute "!gconftool-2 --type string --set /apps/gnome-terminal/profiles/Default/cursor_shape block"
  au VimEnter * silent execute "!gconftool-2 --type string --set /apps/gnome-terminal/profiles/Default/cursor_shape block"
endif

"press jj to exit from insert mode
inoremap jj <Esc> 

"prevent automatically create new new when charactors surpass 512 in one line. this one is of no use
:set tw=0

"automatically add some skeleton codes when creating a .py file
:autocmd BufNewFile  *.py 0r ~/.vim/skeletons/skeleton.py

"new added by myself  - - - - - - - - - - - - - - - - - - - - 

autocmd FileType html setlocal shiftwidth=2 tabstop=2
:set modifiable
"colorscheme Solarized 
:set ts=8 et sw=4 sts=4

"highlight Normal ctermbg=White
highlight Comment ctermbg=DarkGray
"highlight Constant ctermbg=Blue
"highlight Normal ctermbg=Black
"highlight NonText ctermbg=white
highlight Special ctermbg=DarkMagenta
highlight Cursor ctermbg=Green
" this next line is needed to enable your custom colors:
syntax enable

:set pastetoggle=<F3>
"this line avoid unexpected indent and change lines when paste from terminal
"how to use? in the insert mode press F3 and 
"paste the text from the clipboard, then press F3 again

" Linux
set rtp+=~/.vim/bundle/vundle/
"call vundle#rc()
" Windows
" set rtp+=~/vimfiles/bundle/vundle/
" let path='~/vimfiles/bundle'
" call vundle#rc(path)

" let Vundle manage Vundle
" required! 
"Bundle 'gmarik/vundle'
let NERDTreeShowHidden=1
let NERDTreeShowBookmarks=1  
let NERDTreeIgnore=['\.\.$', '\.$', '\~$']  

" My bundles here:
" original repos on GitHub
"Bundle 'scrooloose/nerdtree'
"Bundle 'jistr/vim-nerdtree-tabs'

" non-GitHub repos
" Bundle 'git://git.wincent.com/command-t.git'
" Git repos on your local machine (i.e. when working on your own plugin)
" Bundle 'file:///Users/gmarik/path/to/plugin'
" ...

filetype indent plugin on     " automatic indentation for Python code 
syntax on                     " automatically enable syntax coloring 

" set font
if has("gui_running")
  if has("gui_gtk2")
      set guifont=Inconsolata\ 12
  elseif has("gui_macvim")
      set guifont=Menlo\ Regular:h14
  elseif has("gui_win32")
      set guifont=Consolas:h11:cANSI
  endif
endif
