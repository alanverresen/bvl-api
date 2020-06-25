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
	./scripts/make_help.sh

.PHONY: install-dev
install-dev:
	./scripts/make_install_dev.sh

.PHONY: publish-major
publish-major:
	./scripts/make_requires_dev.sh
	./scripts/make_publish.sh major

.PHONY: publish-minor
publish-minor:
	./scripts/make_requires_dev.sh
	./scripts/make_publish.sh minor

.PHONY: publish-patch
publish-patch:
	./scripts/make_requires_dev.sh
	./scripts/make_publish.sh patch

.PHONE: clean
clean:
	./scripts/make_clean.sh

.PHONE: check
check:
	./scripts/make_requires_dev.sh
	./scripts/make_check.sh
