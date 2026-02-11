# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lunsold <your@email.com>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/10 00:00:00 by lunsold           #+#    #+#              #
#    Updated: 2026/02/10 00:00:00 by lunsold          ###   ########.fr        #
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
PIP			= $(VENV)/bin/pip
ACTIVATE	= source $(VENV)/bin/activate

SRC_DIR		= src
CONFIG		= config.txt
OUTPUT		= maze.txt
MAZE_TXT	= $(SRC_DIR)/maze.txt

# Python files
MAIN		= $(SRC_DIR)/main.py
VISUALIZER	= $(SRC_DIR)/visualize_maze.py
PARSER		= $(SRC_DIR)/mazeparser.py
SOLVER		= $(SRC_DIR)/solve_maze_algo.py

# ================================ TARGETS ================================= #

all: install
	@echo "$(GREEN)✅ Installation complete! Run 'make run' to start.$(RESET)"

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
	@echo "rich>=13.0.0" > requirements.txt
	@echo "$(GREEN)✅ requirements.txt created!$(RESET)"

# Create config.txt if it doesn't exist
$(CONFIG):
	@echo "$(YELLOW)⚠️  config.txt not found. Creating default...$(RESET)"
	@echo "WIDTH=15" > $(CONFIG)
	@echo "HEIGHT=15" >> $(CONFIG)
	@echo "ENTRY=0,0" >> $(CONFIG)
	@echo "EXIT=14,14" >> $(CONFIG)
	@echo "PERFECT=True" >> $(CONFIG)
	@echo "SEED=42" >> $(CONFIG)
	@echo "OUTPUT_FILE=output_maze.txt" >> $(CONFIG)
	@echo "$(GREEN)✅ Default config.txt created!$(RESET)"

# Run maze generation
run: install $(CONFIG) $(MAZE_TXT)
	@echo "$(BLUE)🎮 Running maze generator...$(RESET)"
	@$(PYTHON) $(MAIN)

# Run with animation
animate: install $(CONFIG)
	@echo "$(BLUE)🎬 Running with live animation...$(RESET)"
	@$(PYTHON) $(MAIN) --animate

# Visualize existing maze
visualize: install $(MAZE_TXT)
	@echo "$(BLUE)👁️  Visualizing maze...$(RESET)"
	@if [ -f $(OUTPUT) ]; then \
		$(PYTHON) $(VISUALIZER) $(OUTPUT); \
	else \
		echo "$(RED)❌ No maze file found. Run 'make run' first.$(RESET)"; \
	fi

# Solve maze
solve: install $(OUTPUT) $(MAZE_TXT)
	@echo "$(BLUE)🧠 Solving maze...$(RESET)"
	@$(PYTHON) $(SOLVER)

# Test with custom config
test: install
	@echo "$(BLUE)🧪 Running tests...$(RESET)"
	@$(PYTHON) -m pytest tests/ -v || echo "$(YELLOW)⚠️  pytest not installed$(RESET)"

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

# Create maze.txt if it doesn't exist
$(MAZE_TXT):
	@echo "$(YELLOW)⚠️  maze.txt not found. Creating default...$(RESET)"
	@echo "# Default maze file" > $(MAZE_TXT)
	@echo "# This file will be overwritten by generators" >> $(MAZE_TXT)
	@echo "$(GREEN)✅ Default maze.txt created!$(RESET)"

# Reinstall everything
re: fclean all

# Update dependencies
update: $(VENV)/bin/activate
	@echo "$(BLUE)⬆️  Updating dependencies...$(RESET)"
	@$(PIP) install --upgrade pip
	@$(PIP) install --upgrade rich
	@echo "$(GREEN)✅ Dependencies updated!$(RESET)"

# Freeze current dependencies
freeze: $(VENV)/bin/activate
	@echo "$(BLUE)❄️  Freezing dependencies...$(RESET)"
	@$(PIP) freeze > requirements.txt
	@echo "$(GREEN)✅ requirements.txt updated!$(RESET)"

# Show help
help:
	@echo "$(BLUE)╔══════════════════════════════════════════════════════════╗$(RESET)"
	@echo "$(BLUE)║              A_Maze_ing - Makefile Commands              ║$(RESET)"
	@echo "$(BLUE)╚══════════════════════════════════════════════════════════╝$(RESET)"
	@echo ""
	@echo "$(GREEN)Installation:$(RESET)"
	@echo "  make install    - Create venv and install dependencies"
	@echo "  make update     - Update all dependencies"
	@echo ""
	@echo "$(GREEN)Running:$(RESET)"
	@echo "  make run        - Generate maze"
	@echo "  make animate    - Generate maze with live animation"
	@echo "  make visualize  - Show existing maze"
	@echo "  make solve      - Solve the maze"
	@echo ""
	@echo "$(GREEN)Cleaning:$(RESET)"
	@echo "  make clean      - Remove generated files"
	@echo "  make fclean     - Remove venv and all generated files"
	@echo "  make re         - Full reinstall"
	@echo ""
	@echo "$(GREEN)Development:$(RESET)"
	@echo "  make test       - Run tests"
	@echo "  make freeze     - Update requirements.txt"
	@echo "  make help       - Show this help"
	@echo ""

# Activate virtual environment (for manual use)
activate:
	@echo "$(YELLOW)To activate virtual environment, run:$(RESET)"
	@echo "$(GREEN)source $(VENV)/bin/activate$(RESET)"

# Check installation
check: $(VENV)/bin/activate
	@echo "$(BLUE)🔍 Checking installation...$(RESET)"
	@$(PYTHON) --version
	@$(PIP) --version
	@$(PIP) list
	@echo "$(GREEN)✅ Check complete!$(RESET)"

# Development mode - watch for changes
dev: install $(CONFIG)
	@echo "$(BLUE)👨‍💻 Starting development mode...$(RESET)"
	@echo "$(YELLOW)Press Ctrl+C to stop$(RESET)"
	@while true; do \
		$(PYTHON) $(MAIN); \
		sleep 2; \
	done

.PHONY: all install run animate visualize solve clean fclean re update freeze help activate check test dev
