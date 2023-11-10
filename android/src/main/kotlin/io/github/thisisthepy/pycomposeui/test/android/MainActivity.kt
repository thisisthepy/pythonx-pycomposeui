package io.github.thisisthepy.pycomposeui.test.android

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.currentComposer
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import io.github.thisisthepy.pycomposeui.*
import io.github.thisisthepy.pycomposeui.test.common.App
import io.github.thisisthepy.pycomposeui.test.common.Greeting


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            PythonLauncher {
                moduleNamePreset = "pycomposeui.main"

                Surface(Modifier.fillMaxSize()) {
                    Column(Modifier.fillMaxSize()) {
                        print("-------0-------------------------")
                        println(currentComposer)
                        Text("---------------HEAD---------------")
                        PythonWidget("UiTest", Modifier) {
                            print("-------1-------------------------")
                            println(currentComposer)
                            Column {
                                Text(Greeting().greet()+"khlkhlkgfdgj")
                                Text("                                                               "+Greeting().greet()+"ssss")
                            }
                        }
                        PythonWidget("RichText", Modifier) {
                            print("-------2-------------------------")
                            println(currentComposer)
                            Text(Greeting().greet()+"ssss")
                        }
                        PythonWidget("RichText", Modifier) {
                            PythonWidget("RichText", Modifier) {
                                Column {
                                    Text(Greeting().greet()+"ssss")
                                    Text("                                                               "+Greeting().greet()+"ssss")
                                }
                            }
                            Text("----------------------------------------------2.5")
                        }
                        PythonWidget("RichText", Modifier) {
                            print("-------3-------------------------")
                            println(currentComposer)
                            Column {
                                Text(Greeting().greet()+"ssss")
                                Text("                                                               "+Greeting().greet()+"ssss")
                            }
                        }
                        Text("---------------FOOT---------------")
                    }
                }
            }
        }
    }
}

@Preview
@Composable
fun DefaultPreview() {
    App()
}
