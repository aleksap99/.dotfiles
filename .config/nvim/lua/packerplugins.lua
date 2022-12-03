vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
  use 'wbthomason/packer.nvim'
  use 'windwp/nvim-autopairs'
  use 'kyazdani42/nvim-web-devicons'
  use 'kyazdani42/nvim-tree.lua'
  use 'iamcco/markdown-preview.nvim'
  use 'kevinhwang91/nvim-ufo'
  use 'lambdalisue/suda.vim'
  use 'nvim-lua/plenary.nvim'
  use 'nvim-telescope/telescope.nvim'
  use { 'nvim-telescope/telescope-fzf-native.nvim', run = 'make' }
  use { 'nvim-treesitter/nvim-treesitter', run = ':TSUpdate' }
  use 'williamboman/nvim-lsp-installer'
  use 'neovim/nvim-lspconfig'
  use { 'ms-jpq/coq_nvim', branch='coq' }
  use { 'ms-jpq/coq.artifacts', branch='artifacts' }
  use 'mfussenegger/nvim-jdtls'
  use 'nvim-lualine/lualine.nvim'
  use 'drewtempelmeyer/palenight.vim'
  use { "catppuccin/nvim", as = "catppuccin" }
  use {
    'goolord/alpha-nvim',
    config = function ()
        require'alpha'.setup(require'alpha.themes.dashboard'.config)
    end
  }
end)
