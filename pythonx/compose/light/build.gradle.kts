import org.jetbrains.compose.desktop.application.dsl.TargetFormat

plugins {
    kotlin("jvm").version("2.0.20")
    alias(libs.plugins.jetbrainsCompose)
    alias(libs.plugins.compose.compiler)
    id("com.github.johnrengelman.shadow").version("7.1.2")
}

group = "org.example"
version = "1.0"

repositories {
    google {
        mavenContent {
            includeGroupAndSubgroups("androidx")
            includeGroupAndSubgroups("com.android")
            includeGroupAndSubgroups("com.google")
        }
    }
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))

    implementation(compose.runtime)
    implementation(compose.foundation)
    implementation(compose.material)
    implementation(compose.ui)
    implementation(compose.components.resources)
    implementation(compose.components.uiToolingPreview)
    implementation(libs.androidx.lifecycle.viewmodel)
    implementation(libs.androidx.lifecycle.runtime.compose)

    implementation(compose.desktop.currentOs)
    implementation(libs.kotlinx.coroutines.swing)
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(19)
}

compose.desktop {
    application {
        mainClass = "org.example.project.AppKt"

        nativeDistributions {
            targetFormats(TargetFormat.Dmg, TargetFormat.Msi, TargetFormat.Deb)
            packageName = "org.example.project"
            packageVersion = "1.0.0"
        }
    }
}

tasks.shadowJar {
    manifest {
        attributes(mapOf("Main-Class" to "org.example.project.AppKt"))
    }
}
