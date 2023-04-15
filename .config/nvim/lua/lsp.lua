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

require 'lspconfig'.html.setup {
  on_attach = on_attach
}

require 'lspconfig'.jsonls.setup {
  on_attach = on_attach
}

local metals_config = require("metals").bare_config()

-- Example of settings
metals_config.settings = {
  showImplicitArguments = true,
  excludedPackages = { "akka.actor.typed.javadsl", "com.github.swagger.akka.javadsl" },
}

-- *READ THIS*
-- I *highly* recommend setting statusBarProvider to true, however if you do,
-- you *have* to have a setting to display this in your statusline or else
-- you'll not see any messages from metals. There is more info in the help
-- docs about this
-- metals_config.init_options.statusBarProvider = "on"

-- Example if you are using cmp how to make sure the correct capabilities for snippets are set

metals_config.on_attach = function(client, bufnr)

  keymaps.setLspKeymaps(bufnr)
end

-- Autocmd that will actually be in charging of starting the whole thing
local nvim_metals_group = vim.api.nvim_create_augroup("nvim-metals", { clear = true })
vim.api.nvim_create_autocmd("FileType", {
  -- NOTE: You may or may not want java included here. You will need it if you
  -- want basic Java support but it may also conflict if you are using
  -- something like nvim-jdtls which also works on a java filetype autocmd.
  pattern = { "scala", "sbt" },
  callback = function()
    require("metals").initialize_or_attach(metals_config)
  end,
  group = nvim_metals_group,
})
