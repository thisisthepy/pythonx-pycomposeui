plugins {
    alias(libs.plugins.android.application).apply(false)
    alias(libs.plugins.android.library).apply(false)
    alias(libs.plugins.kotlin.jvm).apply(false)
    alias(libs.plugins.kotlin.android).apply(false)
    alias(libs.plugins.kotlin.multiplatform).apply(false)
    alias(libs.plugins.jetpack.compose).apply(false)

    alias(libs.plugins.chaquo.python).apply(false)
    alias(libs.plugins.moko.resources).apply(false)
}
