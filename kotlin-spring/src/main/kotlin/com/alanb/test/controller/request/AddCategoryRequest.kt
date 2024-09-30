package com.alanb.test.controller.request

import com.fasterxml.jackson.annotation.JsonCreator
import com.fasterxml.jackson.annotation.JsonProperty

data class AddCategoryRequest @JsonCreator(mode = JsonCreator.Mode.PROPERTIES) constructor(
    val name: String,
)
