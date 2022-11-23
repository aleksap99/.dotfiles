require('packerplugins')
require('settings')
require('plugins')
require('lsp')

-- coq settings
local coq = require "coq"
vim.cmd('COQnow -s')

