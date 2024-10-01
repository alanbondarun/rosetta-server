package com.alanb.test.controller.request

import com.fasterxml.jackson.annotation.JsonCreator

data class AddCategoryRequest
    @JsonCreator(mode = JsonCreator.Mode.PROPERTIES)
    constructor(
        val name: String,
    )
