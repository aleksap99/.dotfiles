vim.opt.syntax = "on" 
vim.opt.wrap = false 
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.mouse = "a"
vim.opt.expandtab = true
vim.opt.tabstop = 2
vim.opt.shiftwidth = 2
vim.opt.smartcase = true
vim.opt.hlsearch = true
vim.opt.background = "dark"
vim.opt.termguicolors = true
vim.g.mapleader = "\\"
--vim.opt.ls = 0
--vim.opt.ch = 0

vim.cmd("colorscheme catppuccin-macchiato")
vim.cmd("set updatetime=500")
vim.cmd("hi CursorLineNr guifg=#fcf403")
vim.cmd("set cursorline")
vim.cmd("set cursorlineopt=number")
