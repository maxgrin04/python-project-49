install:
	uv	sync   

brain-games:
	uv	run	brain-games

build:
	uv	build 

package-install:
	uv pip install --reinstall dist/*.whl	

lint:
	uv	run	ruff	check	.

lint-fix:
	uv	run	ruff	check	--fix	.

.PHONY:	lint	install	brain-games	build	package-install