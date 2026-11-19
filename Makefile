# seo-standards: docs-repo verb subset (OMNI-CORE 2, mirroring spec-standards)

VOICE ?= $(HOME)/dev/src/standards/scripts/voice-lint.py

.PHONY: help lint check route ci

help:
	@echo "lint      - voice-lint --strict over all Markdown (SKIP when standards canon absent)"
	@echo "check     - route.py --list parses SEO-CORE and finds >= 60 techniques (catalog integrity)"
	@echo "route     - scripts/route.py --task \"...\" (task-keyword technique lookup)"
	@echo "ci        - lint + check (AGENTS.md rule 7)"

lint:
	@if [ -f "$(VOICE)" ]; then \
		python3 $(VOICE) --strict .; \
	else \
		echo "SKIP: voice-lint not found at $(VOICE)"; \
	fi

check:
	@python3 scripts/route.py --list | wc -l | xargs test 60 -le && echo "route check: catalog parses (>= 60 techniques)"
	@python3 scripts/route.py --eval && echo "route eval: classification regression suite green"

route:
	@if [ -z "$(T)" ]; then echo "usage: make route T=\"migrating a site\""; else python3 scripts/route.py --task "$(T)"; fi

ci: lint check
