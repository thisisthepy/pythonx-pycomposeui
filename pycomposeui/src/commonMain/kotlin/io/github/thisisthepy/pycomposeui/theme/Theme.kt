package io.github.thisisthepy.pycomposeui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.runtime.Composable


@Composable
expect fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = false,
    content: @Composable () -> Unit
)

/*
 * @return true when nighttime or if dark theme is enabled
 */
@Composable
fun isTimeInNightPeriod(): Boolean = isSystemInDarkTheme()// || !isAfter6AMBefore6PM()
