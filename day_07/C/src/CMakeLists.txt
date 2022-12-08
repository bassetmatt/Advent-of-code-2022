add_executable(
    seven seven.c
)

set_target_properties(
    seven
    PROPERTIES 
        RUNTIME_OUTPUT_DIRECTORY  ${PROJECT_SOURCE_DIR}/bin
)