install:
	uv	sync   

brain-games:
	uv	run	brain-games

build:
	uv	build 

package-install:
	uv tool install dist/hexlet_code-0.1.8-py3-none-any.whl	

lint:
	uv	run	ruff	check	.

lint-fix:
	uv	run	ruff	check	--fix	.

.PHONY:	lint	install	brain-games	build	package-install