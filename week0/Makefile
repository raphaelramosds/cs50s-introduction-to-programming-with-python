TARGETS=test-0_indoor \
	test-1_playback

test-%:
	@echo "($*) Running Python tests...\n"
	@if [ -d "$*/python" ]; then cd "$*/python" && pytest; fi

	@echo "($*) Running Go tests...\n"
	@if [ -d "$*/go" ]; then cd "$*/go" && go test ./...; fi

all: $(TARGETS)