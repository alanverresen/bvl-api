#-----------------------------------------------------------------------------
# MAKE SETTINGS
#-----------------------------------------------------------------------------

# first target is the default target, overwrite with help
default: help

# supress command echoes
ifndef VERBOSE
.SILENT:
endif


#-----------------------------------------------------------------------------
# GENERAL TARGETS
#-----------------------------------------------------------------------------

.PHONY: help
help:
	. scripts/make_help.sh

.PHONY: docs
docs:
	. scripts/make_docs.sh

.PHONY: lint
lint:
	. scripts/make_lint.sh

.PHONY: test
test:
	. scripts/make_test.sh

.PHONY: update
update:
	. scripts/make_update.sh

.PHONY: dev
dev:
	. scripts/make_dev.sh

.PHONY: publish
publish:
	. scripts/make_publish.sh
