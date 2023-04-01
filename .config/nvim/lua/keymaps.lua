local map = require("keymapper").map

map("n", "<leader>ff", "<cmd>Telescope find_files<CR>", { silent = true })
map("n", "<leader>fg", "<cmd>Telescope live_grep<CR>", { silent = true })
map("n", "<leader>fb", "<cmd>Telescope buffers<CR>", { silent = true })
map("n", "<leader>fh", "<cmd>Telescope help_tags<CR>", { silent = true })
map("n", "<C-n>", ":NvimTreeToggle<CR>", { silent = true })

-- cant decide whether i like ctrl or alt more
map("i", "<A-a>", "<ESC>I", { silent = true })
map("n", "<A-a>", "<ESC>^", { silent = true })
map("i", "<A-e>", "<ESC>A", { silent = true })
map("n", "<A-e>", "<ESC>$", { silent = true })
map("i", "<C-a>", "<ESC>I", { silent = true })
map("n", "<C-a>", "<ESC>^", { silent = true })
map("i", "<C-e>", "<ESC>A", { silent = true })
map("n", "<C-e>", "<ESC>$", { silent = true })

map("v", "<C-c>", '"+y <ESC>', { silent = true })
map("i", "<C-d>", '<Del>', { silent = true })

local M = {}

function M.setLspKeymaps(bufnr)
  local bufopts = { noremap = true, silent = true, buffer = bufnr }
  vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, bufopts)
  vim.keymap.set('n', 'gd', vim.lsp.buf.definition, bufopts)
  vim.keymap.set('n', 'K', vim.lsp.buf.hover, bufopts)
  vim.keymap.set('n', 'gi', vim.lsp.buf.implementation, bufopts)
  vim.keymap.set('n', '<C-k>', vim.lsp.buf.signature_help, bufopts)
  vim.keymap.set('n', '<leader>wa', vim.lsp.buf.add_workspace_folder, bufopts)
  vim.keymap.set('n', '<leader>wr', vim.lsp.buf.remove_workspace_folder, bufopts)
  vim.keymap.set('n', '<leader>wl', function()
    print(vim.inspect(vim.lsp.buf.list_workspace_folders()))
  end, bufopts)
  vim.keymap.set('n', '<leader>D', vim.lsp.buf.type_definition, bufopts)
  vim.keymap.set('n', '<leader>rn', vim.lsp.buf.rename, bufopts)
  vim.keymap.set('n', '<leader>ca', vim.lsp.buf.code_action, bufopts)
  vim.keymap.set('n', 'gr', vim.lsp.buf.references, bufopts)
  vim.keymap.set('n', '<leader>rr', function() vim.lsp.buf.format { async = true } end, bufopts)

  local opts = { noremap = true, silent = true }
  vim.keymap.set('n', '<leader>e', vim.diagnostic.open_float, opts)
  vim.keymap.set('n', '[d', vim.diagnostic.goto_prev, opts)
  vim.keymap.set('n', ']d', vim.diagnostic.goto_next, opts)
  vim.keymap.set('n', '<leader>q', vim.diagnostic.setloclist, opts)
  vim.keymap.set('n', '<leader>ea', vim.diagnostic.setqflist, opts)
end

return M
