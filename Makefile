# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdreissi <jdreissi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/10 00:00:00 by lunsold           #+#    #+#              #
#    Updated: 2026/03/02 19:24:01 by jdreissi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ================================ COLORS ================================== #
RED		= \033[0;31m
GREEN	= \033[0;32m
YELLOW	= \033[0;33m
BLUE	= \033[0;34m
RESET	= \033[0m

# ================================ VARIABLES =============================== #
VENV		= venv
PYTHON		= $(VENV)/bin/python3
DEGUGG_MODE	= $(VENV)/bin/python3 -m pdb
PIP			= $(VENV)/bin/pip
ACTIVATE	= source $(VENV)/bin/activate

lint1		= flake8 .
lint2		= mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
SRC_DIR		= src
OUTPUT		= maze.txt
MAZE_TXT	= $(SRC_DIR)/maze.txt

# Python files
MAIN		= a_maze_ing.py

# ================================ TARGETS ================================= #

all: run

# Install dependencies in virtual environment
install: $(VENV)/bin/activate requirements.txt
	@echo "$(BLUE)📦 Installing dependencies...$(RESET)"
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requirements.txt
	@echo "$(GREEN)✅ Dependencies installed successfully!$(RESET)"
	@echo "$(YELLOW)💡 Virtual environment created at: $(VENV)$(RESET)"

# Create virtual environment
$(VENV)/bin/activate:
	@echo "$(BLUE)🔧 Creating virtual environment...$(RESET)"
	@python3 -m venv $(VENV)
	@echo "$(GREEN)✅ Virtual environment created!$(RESET)"

# Create requirements.txt if it doesn't exist
requirements.txt:
	@echo "$(BLUE)📝 Creating requirements.txt...$(RESET)"
	@echo "rich>=13.0.0\npytest>=7.0.0\nneovim>=0.3.1\npyfiglet>=0.8.post1\nasciimatics>=1.1.0" > requirements.txt
	@echo "$(GREEN)✅ requirements.txt created!$(RESET)"
	@echo "$(GREEN)✅ richui, pytest, neovim, and pyfiglet installed successfully!$(RESET)"
# Create config.txt if it doesn't exist

# Run maze generation
run: install $(CONFIG)
	@echo "$(BLUE)🎮 Running maze generator...$(RESET)"
	@PYTHONPATH=$(SRC_DIR) $(PYTHON) $(MAIN)

debug: install 
	echo
	$(DEGUGG_MODE) a_maze_ing.py

# Clean generated files
clean:
	@echo "$(YELLOW)🧹 Cleaning generated files...$(RESET)"
	@rm -f $(OUTPUT)
	@rm -f $(MAZE_TXT)
	@rm -rf __pycache__
	@rm -rf $(SRC_DIR)/__pycache__
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@echo "$(GREEN)✅ Cleaned!$(RESET)"

# Clean everything including venv
fclean: clean
	@echo "$(RED)🗑️  Removing virtual environment...$(RESET)"
	@rm -rf $(VENV)
	@rm -f requirements.txt
	@echo "$(GREEN)✅ Full clean complete!$(RESET)"
 
# Reinstall everything
re: fclean all

# check the code with flake8 and mypy
lint:
	@echo "$(BLUE)🔍 Running linters...$(RESET)"
	@$(lint1)
	@$(lint2)
	@echo "$(GREEN)✅ Linting complete!$(RESET)"

# Show help
help:
	@echo "$(BLUE)╔══════════════════════════════════════════════════════════╗$(RESET)"
	@echo "$(BLUE)║              A_Maze_ing - Makefile Commands              ║$(RESET)"
	@echo "$(BLUE)╚══════════════════════════════════════════════════════════╝$(RESET)"
	@echo ""
	@echo "$(GREEN)Installation:$(RESET)"
	@echo "  make install    - Create venv and install dependencies"
	@echo ""
	@echo "$(GREEN)Running:$(RESET)"
	@echo "  make run        - Generate maze"
	@echo ""
	@echo "$(GREEN)Cleaning:$(RESET)"
	@echo "  make clean      - Remove generated files"
	@echo "  make fclean     - Remove venv and all generated files"
	@echo "  make re         - Full reinstall"
	@echo ""

.PHONY: all install run clean fclean re help activate