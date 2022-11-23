require("nvim-lsp-installer").setup({
    automatic_installation = true,
    ui = {
        icons = {
            server_installed = "✓",
            server_pending = "➜",
            server_uninstalled = "✗"
        }
    }
})

require("nvim-autopairs").setup()

require'nvim-web-devicons'.setup {
 color_icons = true;
 default = true;
}

require("lualine").setup{
  options = {
    icons_enabled = true,
    theme = 'auto',
  }
}

require('telescope').setup {
  extensions = {
    fzf = {
      fuzzy = true,
      override_generic_sorter = true,
      override_file_sorter = true,
      case_mode = "smart_case",
    }
  },
	pickers = {
		find_files = {
			hidden = true,
		}
	}
}

require('telescope').load_extension('fzf')

require'nvim-treesitter.configs'.setup {
	  ensure_installed = { "java", "typescript", "python", "go" },
		highlight = {
			enable = true,
		},
}

require("nvim-tree").setup()

