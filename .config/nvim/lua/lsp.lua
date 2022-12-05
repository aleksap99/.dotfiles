local keymaps = require('keymaps')
local coq = require "coq"

local on_attach = function(client, bufnr)
  vim.api.nvim_buf_set_option(bufnr, 'omnifunc', 'v:lua.vim.lsp.omnifunc')
  keymaps.setLspKeymaps(bufnr)
end

local lsp_flags = {
  allow_incremental_sync = true,
  debounce_text_changes = 150,
}

require 'lspconfig'['tsserver'].setup(coq.lsp_ensure_capabilities({
  on_attach = on_attach,
}))

require 'lspconfig'.jdtls.setup {
  on_attach = on_attach,
}

require 'lspconfig'.gopls.setup {
  on_attach = on_attach,
}

require 'lspconfig'.pyright.setup {
  on_attach = on_attach,
}

require 'lspconfig'.sumneko_lua.setup {
  on_attach = on_attach,
  settings = {
    Lua = {
      workspace = {
        -- Make the server aware of Neovim runtime files
        library = vim.api.nvim_get_runtime_file("", true),
      },
    }
  }
}
